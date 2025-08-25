find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_SIGMF gnuradio-sigmf)

FIND_PATH(
    GR_SIGMF_INCLUDE_DIRS
    NAMES gnuradio/sigmf/api.h
    HINTS $ENV{SIGMF_DIR}/include
        ${PC_SIGMF_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_SIGMF_LIBRARIES
    NAMES gnuradio-sigmf
    HINTS $ENV{SIGMF_DIR}/lib
        ${PC_SIGMF_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-sigmfTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_SIGMF DEFAULT_MSG GR_SIGMF_LIBRARIES GR_SIGMF_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_SIGMF_LIBRARIES GR_SIGMF_INCLUDE_DIRS)
