import os

# 1. 파일들이 들어있는 폴더 경로를 지정합니다.
# 현재 파이썬 스크립트와 같은 폴더에 파일이 있다면 '.' 을 사용하세요.
# 다른 폴더에 있다면 절대 경로를 입력하세요. (예: 'C:/Users/Desktop/my_files')
folder_path = '.' 

# 지정된 폴더 내의 모든 파일을 하나씩 확인합니다.
for filename in os.listdir(folder_path):
    
    # 파일 이름에 '-M.'이 포함되어 있는지 확인합니다.
    if '-M.' in filename:
        # '-M.' 부분을 '-mega.'로 바꾼 새로운 파일 이름을 만듭니다.
        new_filename = filename.replace('-M.', '-mega.')
        
        # 파일이 있는 전체 경로를 합쳐줍니다.
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # 파일 이름을 실제로 변경합니다.
        os.rename(old_file, new_file)
        
        # 변경된 내역을 화면에 출력합니다.
        print(f"변경 완료: {filename} -> {new_filename}")

print("모든 파일 이름 변경 작업이 끝났습니다!")