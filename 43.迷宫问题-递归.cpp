/*
深度优先搜索递归解法
https://www.bilibili.com/video/BV1bK4y1C7W2/?spm_id_from=333.337.search-card.all.click
*/
#include <iostream>
#include <vector>
using namespace std;
int n,m,p,q,min_step=99999999;
int** maze;
int** visit;

class Point{
public:
    int m_x, m_y;
    Point(int x, int y){
        m_x = x;
        m_y = y;
    }
};

vector<Point> stack;
vector<Point> min_stack;

void dfs(int x, int y, int step)
{
    if(x==p && y==q){
        if(step<min_step){
            min_step = step;
            min_stack = stack;
        }
        return;
    }
    //顺时针试探
    //右
    if(y+1<m && maze[x][y+1]==0 && visit[x][y+1]==0){
        visit[x][y+1] = 1;
        stack.emplace_back(Point(x,y+1));
        dfs(x,y+1,step+1);
        visit[x][y+1] = 0;
        stack.pop_back();
    }
    //下
    if(x+1<n && maze[x+1][y]==0 && visit[x+1][y]==0){
        visit[x+1][y] = 1;
        stack.emplace_back(Point(x+1,y));
        dfs(x+1,y,step+1);
        visit[x+1][y] = 0;
        stack.pop_back();
    }
    //左
    if(y-1>0 && maze[x][y-1]==0 && visit[x][y-1]==0){
        visit[x][y-1] = 1;
        stack.emplace_back(Point(x,y-1));
        dfs(x,y-1,step+1);
        visit[x][y-1] = 0;
        stack.pop_back();
    }
    //上
    if(x-1>0 && maze[x-1][y]==0 && visit[x-1][y]==0){
        visit[x-1][y] = 1;
        stack.emplace_back(Point(x-1,y));
        dfs(x-1,y,step+1);
        visit[x-1][y] = 0;
        stack.pop_back();
    }
}

int main() {
    cin >> n >> m;
    p=n-1;
    q=m-1;
    //1表示墙壁，0表示可以走的路
    maze = new int*[n];
    //0表示未访问，1表示已访问
    visit = new int*[n];
    for(int i=0;i<n;i++){
        maze[i] = new int[m];
        visit[i] = new int[m];
        for(int j=0;j<m;j++){
            cin >> maze[i][j];
            visit[i][j] = 0;
        }
    }
    visit[0][0]=1;
    stack.emplace_back(Point(0,0));
    dfs(0,0,0);
    //cout<<min_step<<endl;
    for(auto it=min_stack.begin();it!=min_stack.end();it++){
        cout <<'(' << it->m_x << ',' << it->m_y << ')' << endl;
    }
    return 0;
}
