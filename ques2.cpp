
#include<bits/stdc++.h>
using namespace std;

    int maxScore(vector<int>& cardPoints, int k) {
        int sum=0,ans=0;
        int n=cardPoints.size();
        for(int i=0;i<k;i++){
            sum+=cardPoints[i];
        }
        
        ans=sum;
        for(int i=k-1;i>=0;i--){
            sum-=cardPoints[i];
            sum+=cardPoints[n-k+i];
            ans=max(ans,sum);
        }
        
        return ans;
    }

int main(){
    
    vector<int>cardPoints1={1,2,3,4,5,6,1};
    int k1=3;
    
    vector<int>cardPoints2={2,2,2};
    int k2=2;
    
    vector<int>cardPoints3={9,7,7,9,7,7,9};
    int k3=7;
    
    
    
    
    
    
    cout<<maxScore(cardPoints1,k1)<<endl;
    cout<<maxScore(cardPoints2,k2)<<endl;
    cout<<maxScore(cardPoints3,k3)<<endl;
    
    return 0;
    
}