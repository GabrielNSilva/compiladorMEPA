program teste;

var 
    a1,b2,c3 : integer;

begin
    read(a1);
    b2:=a1*2;
    if (b2 > 10)
        begin
            c3:=b2*3;
            write(c3);
        end
    else
        begin
            c3:=a1+b2;
            write(c3);
        end;
end.