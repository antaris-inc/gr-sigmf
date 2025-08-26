# gr-sigmf

This is and out-of-tree gnuradio module that provides block(s) for utilizing sigmf formatted IQ recording files. It makes use of the official sigmf python repository found here: https://github.com/sigmf/sigmf-python and the official spec here: https://github.com/sigmf/SigMF

## Installation
This block requires python installs found in the requirements.txt file, install using pip:

```
pip -r install requirements.txt
```
## ## Development

This module was generated using `gr_modtool`, which means there is a ton of unused scaffolding code here.
Most ongoing development will focus on files in two locations:

* The actual python code implementing the gnuradio blocks is located in files prefixed with `sigmf_` in `./python/sigmf/`
* The GRC configs located in `./grc`, which allow usage of the blocks in GNU Radio Companion (GRC)

