module example_module
#ifndef dp
  use, intrinsic :: iso_fortran_env, only: dp=>real64
#endif

    implicit none


    real(dp) :: example_double
    !! an example double

    real(dp) :: example_double_nodescr

    real(dp) :: example_double_uninit
    !! another example double (uninitialised)

    real(dp), dimension(2) :: example_double_array
    !! an example double array

    real(dp), dimension(2) :: example_double_array_uninit

    integer :: example_int
    !! and example integer
    !! with a description over two lines

    integer :: example_int_uninit
    !! yet another integer

    character*10 :: example_string
    !! and example string

    character*10 :: example_string_uninit
    !! another example string (uninitialised)


    contains

    subroutine init_example_variables
        example_double = 0.0D0
        example_double_nodescr = 1.5D1

        example_int = 5

        example_string = 'string____'
    end subroutine init_example_variables



end module example_module
