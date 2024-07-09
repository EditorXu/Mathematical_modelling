function x = coinChange(n)
    dp = ones(1, n + 2) * inf;
    dp(1) = 0;
    for i = 2 : n + 1
        if i >= 3
            dp(i) = min(dp(i), dp(i - 2) + 1);
        end
        if i >= 6
            dp(i) = min(dp(i), dp(i - 5) + 1);
        end
        if i >= 8
            dp(i) = min(dp(i), dp(i - 7) + 1);
        end
    end
    if dp(n + 1) ~= inf
        x = dp(n + 1);
    else
        x = -1;
    end
end
