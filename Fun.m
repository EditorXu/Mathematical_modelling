function f = Fun(x)
    a = [1 4 3 5 9 12 6 20 17 8];
    b = [2 10 8 18 1 4 5 10 8 9];
    f=zeros(10,1);
    for i = 1:10
        f(i) = abs(x(1)-a(i))+abs(x(2)-b(i));
    end
end
