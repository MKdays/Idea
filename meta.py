#설정
save_file = "meta.ini" #설정
target = "Lotto" #설정

#작업경로 설정
import sys, os
app_path = os.path.join(os.path.dirname(sys.argv[0])) #현재 위치 확인
os.chdir(app_path)

#초기화
if os.path.isfile(save_file): raise("기존파일 있음")

#ini파일 저장 관련
import configparser
config = configparser.ConfigParser()
config.read(save_file, encoding="utf-8")

from glob import glob
file_list =  glob(app_path + "/" +  target + "/**", recursive=True)
e = 0
for i in file_list:
    if os.path.isfile(i): #폴더는제외 파일만
        rel_path = os.path.dirname(os.path.relpath(i)) #상대경로
        
        a = rel_path[len(target):] #현재경로는 삭제하고
        b = os.path.basename(i) #상대경로
        c = str(int(os.path.getmtime(i))) #파일 수정 날짜
        
        config.add_section(str(e)) #섹션 생성
        
        config.set(str(e), "a", a) #상대경로
        config.set(str(e), "b", b) #파일명
        config.set(str(e), "c", c) #수정날짜
        
        e = e+1

#저장
configFile = open(save_file, "w", encoding="utf-8")
config.write(configFile) 
configFile.close()

print("완료!")