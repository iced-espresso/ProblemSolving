def solution(record):
    answer = []
    userNameTable = makeUserDict(record)
    answer = makeResult(record, userNameTable)
    return answer

def makeUserDict(record):
    userDict = {}
    for cmdLine in record:
        s = cmdLine.split()
        cmd = s[0]
        if(cmd != "Leave"):
            uid, name = s[1], s[2]
            userDict[uid] = name
    return userDict

def makeResult(record, userNameTable):
    result = []
    printFormat = {'Enter':"님이 들어왔습니다.",
                   'Leave':"님이 나갔습니다."  }
    for cmdLine in record:
        s = cmdLine.split()
        cmd = s[0]
        if(cmd != 'Change'):
            uid = s[1]
            result.append(userNameTable[uid] + printFormat[cmd])
    return result


testRecord = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(testRecord))



### my first code #######
# class CmdLineParser:
#     def __init__(self, cmdLine):
#         self.cmd, *userInfo = cmdLine.split()
#         self.uid = userInfo[0]
#         self.userName = userInfo[1] if len(userInfo) > 1 else ""

# class UserDict:
#     def __init__(self):
#         self.userDict = {}
#     def update(self, cmdInfo:CmdLineParser):
#         if(cmdInfo.cmd == 'Enter'):
#             self.userDict[cmdInfo.uid] = cmdInfo.userName
#         elif(cmdInfo.cmd == 'Change'):
#             self.userDict[cmdInfo.uid] = cmdInfo.userName
        
# def solution(record):
#     answer = []
#     userNameTable = makeUserDict(record)
#     answer = makeResult(record, userNameTable)
#     return answer

# def makeUserDict(record):
#     userNameTable = UserDict()
#     for cmdLine in record:
#         userNameTable.update(CmdLineParser(cmdLine))
#     return userNameTable.userDict

# def makeResult(record, userNameTable):
#     result = []
#     for cmdLine in record:
#         cmdStr = cmdToString(CmdLineParser(cmdLine), userNameTable)
#         if cmdStr != '':
#             result.append(cmdStr) 
#     return result


# def cmdToString(cmdInfo:CmdLineParser, userNameTable:dict):
#     if(cmdInfo.cmd == 'Enter'):
#         return (userNameTable[cmdInfo.uid] + "님이 들어왔습니다.")
#     elif(cmdInfo.cmd == 'Leave'):
#         return (userNameTable[cmdInfo.uid] + "님이 나갔습니다.")
#     else:
#         return ""