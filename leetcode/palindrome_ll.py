class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    if(head.next==None):return 1
    sh=head
    hd=head
    while(hd.next and hd.next.next):
        sh=sh.next
        hd=hd.next.next
    if(hd.next!=None):
        he1= ListNode(0,sh.next)
        sh.next=he1
    curr=sh.next
    nxt=sh
    while(curr):
        print(curr.val,end="->")
        prv=curr.next
        curr.next=nxt
        nxt=curr
        curr=prv
    print(sh.val)
    tc=nxt
    ts=head
    while(tc!=ts):
        print(tc.val,ts.val)
        if(tc.val!=ts.val):return False
        tc=tc.next
        ts=ts.next
    return True


list2=[1,2,3,4,5,6,9,9,6,5,4,3,2,1]
he1=None
x=None
for i in range((len(list2)-1),-1,-1):
    he1= ListNode(list2[i],x)
    x=he1
print(isPalindrome(he1))