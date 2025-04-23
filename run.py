import datetime
import json


def convert_guest_format(raw_guest: dict[str, str]):
    return {'name': raw_guest['name'],
            'check-in': datetime.date.fromisoformat(raw_guest['check-in']),
            'check-out': datetime.date.fromisoformat(raw_guest['check-out'])
            }


def check_capacity(max_capacity: int, raw_guests: list[dict[str, str]]) -> bool:
    n = len(raw_guests)
    guests = [convert_guest_format(g) for g in raw_guests]

    sorted_guests = sorted(guests, key=lambda g: (g['check-in'], g['check-out']))
    in_dates = []
    out_dates = []
    for guest in sorted_guests:
        in_dates.append(guest['check-in'])
        out_dates.append(guest['check-out'])
    in_idx = 0
    out_idx = 0
    taken = 0
    while in_idx < n or out_idx < n:
        if in_idx == n:
            break

        if (out_idx < n) and out_dates[out_idx] <= in_dates[in_idx]:
            taken -= 1
            out_idx += 1
        else:
            if taken < max_capacity:
                taken += 1

                in_idx += 1
            else:
                return False
    return True


if __name__ == "__main__":
    mc = int(input())
    n = int(input())
    g = []
    for _ in range(n):
        guest_dict = json.loads(input())
        g.append(guest_dict)
    result = check_capacity(mc, g)
    print(result)
