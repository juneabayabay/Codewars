function splitCoins(coins, k) {
    // First k coins
    const groupA = coins.slice(0, k);

    // Remaining coins
    const groupB = coins.slice(k);

    // Flip every coin in group A
    groupA.forEach(coin => coin.flip());

    return [groupA, groupB];
}