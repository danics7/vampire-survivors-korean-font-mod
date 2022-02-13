import shutil


def close():
    input("\r\n\r\n만든사람: danics\r\n종료하시려면 Enter 누르세요")
    exit()


if __name__ == '__main__':
    print(
        '=============================================================\r\n' +
        '--------------Vampire Survivor 한글 폰트 모드-------------------\r\n' +
        '=============================================================\r\n\r\n'
          )
    originalPath = '.\\resources\\app\\.webpack\\renderer\\main.bundle.js'
    newPath = '.\\resources\\app\\.webpack\\renderer\\main.bundle.js.new'
    try:
        f = open(originalPath, 'r', encoding='UTF8')

        # 폰트변경
        originalCodes = f.read()
        codes = originalCodes
        f.close()

        codes = codes.replace('Courier', '메이플스토리')

        f = open(newPath, 'w', encoding='UTF-8')
        f.write(codes)
        f.close()
        shutil.move(newPath, originalPath)

        print("폰트는 넥슨의 메이플스토리체로 변경되었으며, 같이 압축된 Maplestory Light.ttf 파일을 실행해서 설치해주세요.")
        close()
    except FileNotFoundError:
        print('main.bundle.js를 못찾았어요. Vampire Survivors 홈 경로가 맞나요?' +
              '\r\n보통 steamapps\\common\\Vampire Survivors에 있답니다\r\n' +
              '스팀 라이브러리 -> 속성 -> 로컬파일 -> 찾아보기... 하면 나오는 곳에 exe 파일을 위치해주세요')
        close()
