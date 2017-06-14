.model tiny
.data
fname db 'tt.txt',0
myname db 'JAISHIL'
newline db 0dh,0ah
myid db '2015A7PS002G'
hostelname db 'AH3'
roomno db '153'
str1 db 8 dup (?)
handle dw ?
str2 db 10 dup ('$')

createFileH macro fname,att
			mov ah,3ch
			lea dx,fname
			mov cl,att
			int 21h
			endm

openFileH macro fname,mode
			mov ah,3dh
			mov al,mode
			lea dx,fname
			int 21h
			endm

writeFile macro handle,nob,data
			mov ah,40h
			mov bx,handle
			mov cx,nob
			lea dx,data
			int 21h
			endm
			
closeFile macro handle
			mov ah,3eh
			mov bx,handle
			int 21h
			endm
			
readFile macro handle,nob,dest
			mov ah,3fh
			mov bx,handle
			mov cx,nob
			lea dx,dest
			int 21h
			endm

readFileBB macro handle,dest
			mov ah,3fh
			mov bx,handle
			mov cx,1
			mov dx,dest
			int 21h
			endm
			
movePointer macro handle,pos,numH,numL
			mov ah,42h
			mov al,pos
			mov bx,handle
			mov cx,numH
			mov dx,numL
			int 21h
			endm
			
deleteFile macro fname
			mov ah,41h
			lea dx,fname
			int 21h
			endm
			
renameFile macro initial,final,att
			mov ah,56h
			lea dx,initial
			lea di,final
			mov cl,att
			int 21h
			endm
			
.code
.startup	
	;createFileH macro fname,att
	;openFileH macro fname,mode
	;writeFile macro handle,nob,data
	;closeFile macro handle
	;readFile macro handle,nob,dest
	;movePointer macro handle,pos,numH,numL
	;deleteFile macro fname
	;renameFile macro initial,final,att
	;readFileBB macro handle,dest		
			
			;createFileH fname,0
			;openFileH fname,2
			;mov handle,ax
			;writeFile handle,7,myname
			;writeFile handle,2,newline  	;TASK1
			;writeFile handle,12,myid
			;closeFile handle
			
			
			;openFileH fname,2
			;mov handle,ax
			;writeFile handle,3,hostelname
			;writeFile handle,2,newline		;TASK2	
			;writeFile handle,3,roomno
			;closeFile handle
			
			;openFileH fname,2
			;mov handle,ax
			;readFile handle,8,str1			;TASK3	
			;closeFile handle
			
	;		openFileH fname,2
	;		mov handle,ax
	;		lea di,str1
	;	x :	readFileBB handle,di
	;		inc di
	;		cmp ax,0						;TRY AGAIN BC TASK4
	;		je done
	;		cmp ax,cx
	;		jnle x
	;done :	closeFile handle	
			
			
			
.exit
end