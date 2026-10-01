cmake_minimum_required(VERSION 3.20)
project(FreshmanChallenge LANGUAGES CXX)

# 新生只需修改这一行；保留双引号，引号中填自己的学号，不需要加U
set(STUDENT_ID "202615010")

if(NOT STUDENT_ID MATCHES "^[0-9][0-9]+$")
    message(FATAL_ERROR "Set STUDENT_ID in CMakeLists.txt to your student number (at least two digits).")
endif()

set(GENERATED_DIR "${CMAKE_CURRENT_BINARY_DIR}/generated")
file(MAKE_DIRECTORY "${GENERATED_DIR}")
foreach(FILE_NAME IN ITEMS student_config.h student_info.cpp)
    configure_file(
        "${CMAKE_CURRENT_SOURCE_DIR}/templates/${FILE_NAME}.in"
        "${GENERATED_DIR}/${FILE_NAME}"
        @ONLY
    )
endforeach()

set(CHALLENGE_OBJECT "${CMAKE_CURRENT_SOURCE_DIR}/lib/challenge.o")
if(NOT EXISTS "${CHALLENGE_OBJECT}")
    message(FATAL_ERROR "Missing lib/challenge.o. Ask the organizer for the complete task package.")
endif()
set_source_files_properties("${CHALLENGE_OBJECT}" PROPERTIES EXTERNAL_OBJECT TRUE)

add_executable(challenge
    src/main.cpp
    "${GENERATED_DIR}/student_info.cpp"
    "${CHALLENGE_OBJECT}"
)
target_include_directories(challenge PRIVATE
    "${CMAKE_CURRENT_SOURCE_DIR}/include"
    "${GENERATED_DIR}"
)
target_compile_features(challenge PRIVATE cxx_std_11)
# Reduce MinGW runtime DLL dependencies when double-clicking the program.
if(MINGW)
    target_link_options(challenge PRIVATE -static-libgcc -static-libstdc++)
endif()
