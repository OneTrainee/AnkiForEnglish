import argparse

def _main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', help='file name')
    args = parser.parse_args()
    print('Output file:', args.file)


if __name__ == '__main__':
    _main()