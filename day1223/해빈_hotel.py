rooms = [False] * 9 # False = 빈방 기준

while True:
   print("\n===== hotel management system =====")
   print("1. 조회")
   print("2. 입실")
   print("3. 퇴실")
   print("4. 종료")

   menu = input("메뉴 선택: ")       

   if menu == '1':
        print("\n--- 입실 상태 ---")
        for i in range(9): #방 조회
            status = "사용 중" if rooms[i] else "빈 방" #True면 사용중 False면 빈방
            print(f"{i+1}호 : {status}")

   elif menu == '2':
        room = int(input("입실 호수 입력(1~9): "))
        name = input("고객명 입력 : ") # 고객명 저장을 어떻게 해야할지 잘 모르겠음.

        if rooms[room - 1]:
            print(f"{room}호는 입실중 입니다.")
        else: rooms[room - 1] = True
        print(f"{room}호 입실 완료")

   elif menu == '3':
        room = int(input("퇴실 호수 입력(1~9): "))
        if not rooms[room - 1]:
            print(f"{room}호는 빈 방입니다.")
        else: rooms[room - 1] = False
        print(f"{room}호 퇴실 완료")

   elif menu == '4':
        print("프로그램 종료")
        r = open("./day1223/해빈_hotel.txt",'r',encoding="utf-8")
        room = r.read()
        print(room)
        r.close()

        break
            




