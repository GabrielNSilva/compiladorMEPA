program teste;

var a,b,c : integer;

begin
    read(a);
    b:=a*2;
    if (b > 10)
        begin
            c:=b*3;
            write(c);
        end
    else
        begin
            c:=a+b;
            write(c);
        end;
end.