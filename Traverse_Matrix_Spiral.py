import sys

def spiral_order(matrix):
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left along the bottom row
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top along the left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

def main():
    input = sys.stdin.read().strip().split()
    n = int(input[0])
    matrix = []
    index = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input[index]))
            index += 1
        matrix.append(row)
    
    result = spiral_order(matrix)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
