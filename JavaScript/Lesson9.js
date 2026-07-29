function arrayPacking(a) {

    // This variable will store the final packed integer.
    let M = 0;

    // Loop through each number in the array.
    for (let i = 0; i < a.length; i++) {

        /*
         * Each number occupies exactly 8 bits (1 byte).
         *
         * Position of each element:
         *
         * a[0] -> bits 0 - 7
         * a[1] -> bits 8 - 15
         * a[2] -> bits 16 - 23
         * a[3] -> bits 24 - 31
         *
         * To move a number into its correct position,
         * shift it left by (8 * i) bits.
         */

        let shiftedValue = a[i] << (8 * i);

        /*
         * Example:
         *
         * a = [24, 85, 0]
         *
         * i = 0
         * 24 << 0
         * = 00011000
         *
         * i = 1
         * 85 << 8
         * = 01010101 00000000
         *
         * i = 2
         * 0 << 16
         * = 00000000
         */

        /*
         * Combine the shifted value with the current result.
         *
         * The OR (|) operator merges the bits together without
         * affecting the bits that are already set.
         */

        M |= shiftedValue;
    }

    /*
     * JavaScript stores the result of bitwise operations as
     * a signed 32-bit integer.
     *
     * If the highest bit (bit 31) becomes 1, JavaScript treats
     * the number as negative.
     *
     * Using >>> 0 converts the signed integer into its
     * unsigned 32-bit representation.
     *
     * Example:
     *
     * Before:
     * -1626450840
     *
     * After:
     * 2668516456
     */

    return M >>> 0;
}