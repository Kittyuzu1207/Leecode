#假设你正在读取一串整数。每隔一段时间，你希望能找出数字 x 的秩(小于或等于 x 的值的个数)。
#请实现数据结构和算法来支持这些操作，也就是说：
#实现 track(int x) 方法，每读入一个数字都会调用该方法；
#实现 getRankOfNumber(int x) 方法，返回小于或等于 x 的值的个数

#My:简单粗暴用列表存储，每次判断都要遍历一次
class StreamRank:

    def __init__(self):
        self.data=[]

    def track(self, x: int) -> None:
        self.data.append(x)

    def getRankOfNumber(self, x: int) -> int:
        return len([a for a in self.data if a<=x])


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)

#其他：
#法1：树状数组
#由于需要考虑 x=0 的情况，而如果直接将 x=0 传入 query 方法则会陷入死循环，
#故插入和查询时都将输入参数 + 1，防止 query 陷入死循环。
class StreamRank:
    def __init__(self):
        self.a=[0]*50010
    def track(self, x: int) -> None:
        x+=1
        i=x
        while i<len(self.a):
            self.a[i]+=1
            i+=i&(-i)  #i&(-i) 该数的从右往左数第一个为 1 的位的权值,是取i的二进制末尾0个数
    def getRankOfNumber(self, x: int) -> int:
        x+=1
        ans=0
        i=x
        while i>0:
            ans+=self.a[i]
            i-=i&(-i)
        return ans
 
 #?树状数组
 #用数组来模拟树形结构，用于查询任意两位之间的所有元素之和
 #修改和查询的复杂度都是O(logN)
 #[img]https://img2018.cnblogs.com/blog/1448672/201810/1448672-20181003121604644-268531484.png
 #C是树状数组，A是原数组
 #C[i] = A[i - 2^k+1] + A[i - 2^k+2] + ... + A[i];   //k为i的二进制中从最低位到高位连续零的长度
 #2^k = i&(-i)
 #求原数组前i项和
 #SUMi = C[i] + C[i-2k1] + C[(i - 2k1) - 2k2] + ...
 
#法2：二分插排，维护有序数组，每次求上界
class StreamRank {
   public:
    StreamRank() {}

    void track(int x) {
        nums.push_back(x);
        // 插入排序
        for (int i = nums.size() - 1; i > 0; i--) {
            if (nums[i] < nums[i - 1]) {
                swap(nums[i], nums[i - 1]);
            }
        }
    }

    int getRankOfNumber(int x) {
        int left = 0, right = nums.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

   private:
    vector<int> nums;
};

