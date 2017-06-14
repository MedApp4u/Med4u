.model tiny
.486
.data
	fname db "f.txt",0
	
	handle dw ?
	
	w db 30
	we db ?
	wst db 31 dup(0)
	
	b db 2
	be db ?
	bst db 3 dup('$')
	
	r db 9 dup('$')
	t1 db "Manan Pachchigar,2015a7ps037g",0dh,0ah,"Manan Pachchigar,2015a7ps037g",0
	disnl db 0DH,0AH,'$'
	
	o db 61 dup('$')
	
	
input macro x
	lea dx,x
	mov ah,0ah
	int 21h
	endm
	
output macro x 
	lea dx,x
	mov ah,09h
	int 21h
	endm
	
newline macro
	lea dx,disnl
	mov ah,09h
	int 21h
	endm
	
	
createFile macro fname,att	
	mov ah,3ch
	lea dx,fname
	mov cl,att
	int 21h
	mov handle,ax
	endm
	
openFile macro fname,asm	;asm=access and sharing mode,x=fname
	mov ah,3dh
	mov al,asm
	lea dx,fname
	int 21h
	mov handle,ax
	endm
	
closeFile macro fh
	mov ah,3eh
	mov bx,fh
	int 21h
	endm
	
writeInFile macro fh ;No need to give count, type whatever you want
	input w
	mov ah,40h
	mov bx,fh
	lea dx,wst
	lea si,wst
	mov cx,0
x1:	lodsb
	cmp al,0
	je x2
	inc cx
	jmp x1
x2:	nop
	int 21h
	endm
	
writeFile macro fh,nob,data	;Give count
	mov ah,40h
	mov bx,fh
	mov cx,nob
	lea dx,data
	int 21h
	endm
	
readFile macro fh,dest	;Take input of how many characters are to be read
	input b
	mov ah,3fh
	mov bx,fh
	lea si,bst
	mov cx,[si]
	and cx,000fh
	lea dx,dest
	int 21h
	endm
	
readFileGC macro handle,nob,dest	;Give number of characters
	mov ah,3fh
	mov bx,handle
	mov cx,nob
	lea dx,dest
	int 21h
	endm
	
readWholeFile macro handle,o	;Read Bit by bit till EOF
	mov bx,handle
	lea dx,o
x1:	mov ah,3fh
	mov cx,1
	int 21h
	inc dx
	cmp ax,0
	jne x1 
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
	openFile fname,2
	;readFile handle,o
	;readFileGC handle,3,o
	readWholeFile handle,o
	output o
	closeFile handle
	deleteFile fname
.exit
end