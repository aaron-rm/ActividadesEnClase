/ Proyecto final
      / Intrucciones de la maquina PC1

      add  r10 r11 r0		/ R10 = R11 + r0 
      sub r2 r2 r10		/ R2 = R2 - r10        
      and r12 r15 r10      	/ R12 = R15 & R10
      or  r6 r5 r4         	/ R6 = R5 | R6
      sr r2 r1	       		/ R2 = R1 >> 1
      sl r2 r1			/ R2 = R1 << 1
      slt r15 r10		/ R5 < R6 ?
      eq r2 r0			/ R2 == r0 ?        
:in1  sb r0 r1             	/ R0 = *R1
      lb r2 r1             	/ r2 = *r1
      li r10 0 1		/ r10 = 01
      lui r1 0 0		/ r1 = 00
      bra sb1              	/ SI? Salta a la etiqueta SB1  
      jr r15			/ SALTA A *R15 
      spc  r14             	/ R14 = SPC = 4       
	/ Intruccioes de la maquina PC 2  

:rt   mul r15 r15 r10		/ R15 = R15 * 1 
      div r3 r2 r1         	/ R3 = R2 / R1	 
      rem r1 r2 r3         	/ R1 = R2 % R3	 
      xor r1 r5 r11        	/ R1 = R5 ^ R11
      rr r3 r3             	/ R3 rd R3
      rl r5 r5             	/ R5 ri R5
      sgt r5 r6            	/ R5 > R6 ?
      neq r5 r6           	/ R5 != R6 
:sb1  mov r0 r1			/ R0 = R1
      swp r5 r6            	/ R5 = r6(low)<=>R6(high) 
      bra rt			/ SI? salta a rt ciclo infinito            
      bra in1			/ SI? salta a in1 
      and r4 r5 r6         	/ R4 = R5 & R6
      bbr r1               	/ Salta a *R1, Si Bbit es cierto 
      rst 			/ Limpia todos los registros 
      cls 			/ Limpia la TTY
:fi   jmp fi               	/ Fin del programa
	 