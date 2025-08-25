#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2025 gr-sigmf author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr
from gnuradio import blocks
from sigmf import SigMFFile
from sigmf.utils import get_data_type_str, get_sigmf_iso8601_datetime_now


class sigmfSink(gr.hier_block2):
    """
    Custom block using the sigmf python library https://github.com/sigmf/sigmf-python
    """
    def __init__(self, item_size, filename, sample_rate, center_freq, author, description, hw_info, is_complex):
        # Input type, which is included in .sigmf-meta file
        if item_size == 8:
            datatype_str = 'cf32_le'
        elif item_size == 4:
            datatype_str = 'rf32_le'
        elif item_size == 2 and is_complex:
            datatype_str = 'ci16_le'
        elif item_size == 2 and not is_complex:
            datatype_str = 'ri16_le'
        else:
            raise ValueError

        if '.sigmf' in filename:
            filename = filename.rsplit('.', 1)[0]
        gr.log.info(f'Generating {filename}.sigmf-meta, writing SigMF data to {filename}.sigmf-data')

        gr.hier_block2.__init__(self, "sigmf_sink_minimal",
                                gr.io_signature(1, 1, item_size),
                                gr.io_signature(0, 0, 0))

        # use regular File Sink, no append. This handles the data file saving.
        file_sink = blocks.file_sink(
            item_size, filename + '.sigmf-data', False)
        self.connect(self, file_sink)

        meta = SigMFFile(
            global_info = {
                SigMFFile.DATATYPE_KEY: datatype_str,  # in this case, 'cf32_le'
                SigMFFile.SAMPLE_RATE_KEY: sample_rate,
                SigMFFile.AUTHOR_KEY: author,
                SigMFFile.DESCRIPTION_KEY: description,
                SigMFFile.HW_KEY: hw_info
            }
        )

        # create a capture key at time index 0
        meta.add_capture(0, metadata={
            SigMFFile.FREQUENCY_KEY: center_freq,
            SigMFFile.DATETIME_KEY: get_sigmf_iso8601_datetime_now(),
            SigMFFile.START_INDEX_KEY: 0,
        })

        meta.tofile(filename) # file extension is automatically handled by sigmf library.
