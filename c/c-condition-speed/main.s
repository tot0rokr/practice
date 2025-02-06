	.file	"main.c"
	.text
	.globl	add
	.type	add, @function
add:
.LFB23:
	.cfi_startproc
	endbr64
	testl	%edi, %edi
	jle	.L2
	movl	$0, %eax
.L3:
	addl	$1, %eax
	cmpl	%eax, %edi
	jne	.L3
.L2:
	ret
	.cfi_endproc
.LFE23:
	.size	add, .-add
	.globl	condition1
	.type	condition1, @function
condition1:
.LFB24:
	.cfi_startproc
	endbr64
	testl	%edi, %edi
	jle	.L6
	movl	$0, %eax
.L7:
	addl	$1, %eax
	cmpl	%eax, %edi
	jne	.L7
.L6:
	ret
	.cfi_endproc
.LFE24:
	.size	condition1, .-condition1
	.globl	condition2
	.type	condition2, @function
condition2:
.LFB25:
	.cfi_startproc
	endbr64
	testl	%edi, %edi
	jle	.L10
	movl	$0, %eax
.L11:
	addl	$1, %eax
	cmpl	%eax, %edi
	jne	.L11
.L10:
	ret
	.cfi_endproc
.LFE25:
	.size	condition2, .-condition2
	.globl	measure
	.type	measure, @function
measure:
.LFB26:
	.cfi_startproc
	endbr64
	pushq	%r14
	.cfi_def_cfa_offset 16
	.cfi_offset 14, -16
	pushq	%r13
	.cfi_def_cfa_offset 24
	.cfi_offset 13, -24
	pushq	%r12
	.cfi_def_cfa_offset 32
	.cfi_offset 12, -32
	pushq	%rbp
	.cfi_def_cfa_offset 40
	.cfi_offset 6, -40
	pushq	%rbx
	.cfi_def_cfa_offset 48
	.cfi_offset 3, -48
	subq	$16, %rsp
	.cfi_def_cfa_offset 64
	movl	%edi, %r12d
	testl	%edi, %edi
	jle	.L14
	movl	%esi, %r13d
	movq	%rdx, %r14
	movl	$0, %ebp
.L15:
	call	clock@PLT
	movq	%rax, %rbx
	movl	%r13d, %edi
	call	*%r14
	call	clock@PLT
	subq	%rbx, %rax
	pxor	%xmm0, %xmm0
	cvtsi2sdq	%rax, %xmm0
	addsd	8(%rsp), %xmm0
	movsd	%xmm0, 8(%rsp)
	addl	$1, %ebp
	cmpl	%ebp, %r12d
	jne	.L15
.L14:
	pxor	%xmm1, %xmm1
	cvtsi2sdl	%r12d, %xmm1
	movsd	8(%rsp), %xmm0
	divsd	%xmm1, %xmm0
	addq	$16, %rsp
	.cfi_def_cfa_offset 48
	popq	%rbx
	.cfi_def_cfa_offset 40
	popq	%rbp
	.cfi_def_cfa_offset 32
	popq	%r12
	.cfi_def_cfa_offset 24
	popq	%r13
	.cfi_def_cfa_offset 16
	popq	%r14
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE26:
	.size	measure, .-measure
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"add"
.LC1:
	.string	"%s: %lf\n"
.LC2:
	.string	"condition1"
.LC3:
	.string	"condition2"
	.text
	.globl	main
	.type	main, @function
main:
.LFB27:
	.cfi_startproc
	endbr64
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	leaq	add(%rip), %rdx
	movl	$100000000, %esi
	movl	$100, %edi
	call	measure
	leaq	.LC0(%rip), %rdx
	leaq	.LC1(%rip), %rbx
	movq	%rbx, %rsi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk@PLT
	leaq	condition1(%rip), %rdx
	movl	$100000000, %esi
	movl	$100, %edi
	call	measure
	leaq	.LC2(%rip), %rdx
	movq	%rbx, %rsi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk@PLT
	leaq	condition2(%rip), %rdx
	movl	$100000000, %esi
	movl	$100, %edi
	call	measure
	leaq	.LC3(%rip), %rdx
	movq	%rbx, %rsi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk@PLT
	movl	$0, %eax
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE27:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
