import json
import sys


def ipranges(lines):
    for line in lines:
        line = line.strip()
        if not line:
            continue
        yield line


def to_amnezia(ipramges):
    return json.dumps(
        [
            {
                "hostname": iprange,
                "ip": "",
            }
            for iprange in ipramges
        ]
    )


def _main():
    print(to_amnezia(ipranges(sys.stdin)))


if __name__ == "__main__":
    _main()
