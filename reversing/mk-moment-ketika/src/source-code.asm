main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 48
        mov     DWORD PTR [rbp-4], 10
        mov     DWORD PTR [rbp-8], 8
        mov     DWORD PTR [rbp-12], 5875
        mov     DWORD PTR [rbp-16], 19
        mov     eax, DWORD PTR [rbp-4]
        imul    eax, DWORD PTR [rbp-8]
        add     eax, eax
        mov     edi, eax
        call    __gnu_cxx::__enable_if<std::__is_integer<int>::__value, double>::__type std::sqrt<int>(int)
        cvttsd2si       eax, xmm0
        mov     DWORD PTR [rbp-20], eax
        mov     eax, DWORD PTR [rbp-4]
        imul    eax, DWORD PTR [rbp-16]
        add     eax, eax
        mov     edi, eax
        call    __gnu_cxx::__enable_if<std::__is_integer<int>::__value, double>::__type std::sqrt<int>(int)
        cvttsd2si       eax, xmm0
        mov     DWORD PTR [rbp-24], eax
        mov     eax, DWORD PTR [rbp-12]
        imul    eax, DWORD PTR [rbp-20]
        mov     DWORD PTR [rbp-28], eax
        mov     eax, DWORD PTR [rbp-12]
        imul    eax, DWORD PTR [rbp-24]
        mov     DWORD PTR [rbp-32], eax
        mov     eax, DWORD PTR [rbp-32]
        sub     eax, DWORD PTR [rbp-28]
        mov     DWORD PTR [rbp-36], eax
        mov     eax, DWORD PTR [rbp-36]
        imul    eax, eax
        mov     DWORD PTR [rbp-36], eax
        mov     eax, DWORD PTR [rbp-36]
        cmp     eax, DWORD PTR [rbp-32]
        jle     .L2
        mov     eax, DWORD PTR [rbp-36]
        or      eax, 19450817
        add     eax, 177013
        mov     DWORD PTR [rbp-36], eax
        jmp     .L3
.L2:
        mov     eax, DWORD PTR [rbp-36]
        cmp     eax, DWORD PTR [rbp-32]
        jge     .L3
        mov     eax, DWORD PTR [rbp-36]
        or      eax, 17081945
        add     eax, 882370
        mov     DWORD PTR [rbp-36], eax
.L3:
        mov     eax, 0
        leave
        ret
__gnu_cxx::__enable_if<std::__is_integer<int>::__value, double>::__type std::sqrt<int>(int):
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     DWORD PTR [rbp-4], edi
        pxor    xmm1, xmm1
        cvtsi2sd        xmm1, DWORD PTR [rbp-4]
        movq    rax, xmm1
        movq    xmm0, rax
        call    sqrt
        movq    rax, xmm0
        movq    xmm0, rax
        leave
        ret
__static_initialization_and_destruction_0(int, int):
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     DWORD PTR [rbp-4], edi
        mov     DWORD PTR [rbp-8], esi
        cmp     DWORD PTR [rbp-4], 1
        jne     .L9
        cmp     DWORD PTR [rbp-8], 65535
        jne     .L9
        mov     edi, OFFSET FLAT:_ZStL8__ioinit
        call    std::ios_base::Init::Init() [complete object constructor]
        mov     edx, OFFSET FLAT:__dso_handle
        mov     esi, OFFSET FLAT:_ZStL8__ioinit
        mov     edi, OFFSET FLAT:_ZNSt8ios_base4InitD1Ev
        call    __cxa_atexit
.L9:
        nop
        leave
        ret
_GLOBAL__sub_I_main:
        push    rbp
        mov     rbp, rsp
        mov     esi, 65535
        mov     edi, 1
        call    __static_initialization_and_destruction_0(int, int)
        pop     rbp
        ret 
