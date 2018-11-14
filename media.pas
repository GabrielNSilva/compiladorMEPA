// https://pt.wikibooks.org/wiki/Pascal/Estrutura_de_repeti%C3%A7%C3%A3o
program  media_notas;
var
    N1, N2, N3, MEDIA: real;
    CONT: integer;
begin 
    CONT:=0;  
    while CONT<=50 do
    begin
        CONT:=CONT+1;
        read (N1);
        read (N2);
        read (N3);
        MEDIA:=(N1+N2+N3)/3;
        if (MEDIA >= 6) then
            begin
                write(MEDIA);
            end
        else
            write(0);
    end;
end.