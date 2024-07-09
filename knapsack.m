function result = knapsack(weights, values, capacity)
    n = length(weights);
    dp = zeros(n + 1, capacity + 1);
    for i = 2 : n + 1
        for j = 2 : capacity + 1
            if j < weights(i - 1) + 1
                dp(i, j) = dp(i - 1, j);
            else
                dp(i, j) = max(dp(i - 1, j), dp(i - 1, j - weights(i - 1)) + values(i - 1));
            end
        end
    end
    result = dp(n + 1, capacity + 1);
end

