import sys

keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]


def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]


def solve(data):
    robots = []
    all_keys = set()

    for row, line in enumerate(data):
        for col, val in enumerate(line):
            val: str
            if val == '@':
                robots.append((col, row))
            elif val.isalpha() and val.islower():
                all_keys.add(val)

    n = len(robots)
    robot = 0
    keys = set()

    visited = set()

    width = len(data[0])
    height = len(data)
    queues = [[(robots[i], 0)] for i in range(n)]

    last_robot_step = [0 for _ in range(n)]
    while keys != all_keys:
        # print(last_robot_step)
        queue = queues[robot]
        robot = (robot + 1) % n

        if not any(queues):
            raise Exception
        if not queue:
            continue

        (cx, cy), steps = queue.pop(0)
        current = data[cy][cx]
        if current in visited:
            continue
        elif current == '#':
            visited.add((cx, cy))
            continue
        elif current.isupper() and current.lower() not in keys:
            queue.append(((cx, cy), steps + 1))
            continue
        visited.add((cx, cy))
        last_robot_step[robot] = steps
        # print(current)
        if current.isalpha() and current.islower():
            keys.add(current)

        if (cx - 1, cy) not in visited and cx - 1 >= 0:
            queue.append(((cx - 1, cy), steps + 1))
        if (cx + 1, cy) not in visited and cx + 1 < width:
            queue.append(((cx + 1, cy), steps + 1))
        if (cx, cy - 1) not in visited and cy - 1 >= 0:
            queue.append(((cx, cy - 1), steps + 1))
        if (cx, cy + 1) not in visited and cy + 1 < height:
            queue.append(((cx, cy + 1), steps + 1))

    #     print(keys, all_keys)
    # print(data)
    return sum(last_robot_step)


def main():
    data = get_input()
    result = solve(data)
    print(result)


if __name__ == '__main__':
    main()
