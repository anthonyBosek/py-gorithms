# JavaScript Algorithms and Data Structures Projects: Cash Register
#
# Design a cash register drawer function checkCashRegister() that accepts purchase price as the first
# argument (price), payment as the second argument (cash), and cash-in-drawer (cid) as the third argument.
# cid is a 2D array listing available currency. The checkCashRegister() function should always return an
# object with a status key and a change key. Return {status: "INSUFFICIENT_FUNDS", change: []} if cash-in-drawer
# is less than the change due, or if you cannot return the exact change. Return {status: "CLOSED", change: [...]}
# with cash-in-drawer as the value for the key change if it is equal to the change due. Otherwise, return
# {status: "OPEN", change: [...]}, with the change due in coins and bills, sorted in highest to lowest order,
# as the value of the change key.
#
# checkCashRegister(price, cash, cid) ➞ obj


def checkCashRegister(price, cash, cid):
    val = [100, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
    coh = cid[::-1]
    dif = cash - price
    emp = dif == sum([d[1] for d in coh])
    due = []
    for i in range(len(coh)):
        if dif > val[i] and coh[i][1] != 0:
            cnt = 0
            while coh[i][1] > 0 and dif - val[i] >= 0:
                cnt += val[i]
                coh[i][1] -= val[i]
                dif = round(dif - val[i], 2)
            due.append([coh[i][0], cnt])
    return (
        {"status": "INSUFFICIENT_FUNDS", "change": []}
        if dif > 0
        else {"status": "CLOSED", "change": cid}
        if emp
        else {"status": "OPEN", "change": due}
    )


print(
    checkCashRegister(
        190.5,
        500,
        [
            ["PENNY", 1.01],
            ["NICKEL", 2.05],
            ["DIME", 3.1],
            ["QUARTER", 4.25],
            ["ONE", 90],
            ["FIVE", 55],
            ["TEN", 20],
            ["TWENTY", 60],
            ["ONE HUNDRED", 100],
        ],
    )
)
# ➞ an object
print(
    checkCashRegister(
        19.5,
        20,
        [
            ["PENNY", 1.01],
            ["NICKEL", 2.05],
            ["DIME", 3.1],
            ["QUARTER", 4.25],
            ["ONE", 90],
            ["FIVE", 55],
            ["TEN", 20],
            ["TWENTY", 60],
            ["ONE HUNDRED", 100],
        ],
    )
)
# ➞ {status: "OPEN", change: [["QUARTER", 0.5]]}
print(
    checkCashRegister(
        3.26,
        100,
        [
            ["PENNY", 1.01],
            ["NICKEL", 2.05],
            ["DIME", 3.1],
            ["QUARTER", 4.25],
            ["ONE", 90],
            ["FIVE", 55],
            ["TEN", 20],
            ["TWENTY", 60],
            ["ONE HUNDRED", 100],
        ],
    )
)
# ➞ {status: "OPEN", change: [["TWENTY", 60], ["TEN", 20],
#     ["FIVE", 15], ["ONE", 1], ["QUARTER", 0.5], ["DIME", 0.2],
#     ["PENNY", 0.04]]}
print(
    checkCashRegister(
        19.5,
        20,
        [
            ["PENNY", 0.01],
            ["NICKEL", 0],
            ["DIME", 0],
            ["QUARTER", 0],
            ["ONE", 0],
            ["FIVE", 0],
            ["TEN", 0],
            ["TWENTY", 0],
            ["ONE HUNDRED", 0],
        ],
    )
)
# ➞ {status: "INSUFFICIENT_FUNDS", change: []}
print(
    checkCashRegister(
        19.5,
        20,
        [
            ["PENNY", 0.01],
            ["NICKEL", 0],
            ["DIME", 0],
            ["QUARTER", 0],
            ["ONE", 1],
            ["FIVE", 0],
            ["TEN", 0],
            ["TWENTY", 0],
            ["ONE HUNDRED", 0],
        ],
    )
)
# ➞ {status: "INSUFFICIENT_FUNDS", change: []}
print(
    checkCashRegister(
        19.5,
        20,
        [
            ["PENNY", 0.5],
            ["NICKEL", 0],
            ["DIME", 0],
            ["QUARTER", 0],
            ["ONE", 0],
            ["FIVE", 0],
            ["TEN", 0],
            ["TWENTY", 0],
            ["ONE HUNDRED", 0],
        ],
    )
)
# ➞ {status: "CLOSED", change: [["PENNY", 0.5], ["NICKEL", 0],
#     ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0],
#     ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]}
