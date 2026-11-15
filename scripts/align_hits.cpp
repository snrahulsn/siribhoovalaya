#include <vector>
#include <algorithm>
struct Cell { int score, hits; };
static bool better(Cell a, Cell b) { return a.score>b.score || (a.score==b.score && a.hits>b.hits); }
extern "C" int align_hits(const int* a, int n, const int* b, int m) {
    std::vector<Cell> old(m+1), next(m+1);
    for (int j=1;j<=m;j++) old[j]={-2*j,0};
    Cell best={-1000000000,0};
    for (int i=1;i<=n;i++) {
        next[0]={0,0};
        for (int j=1;j<=m;j++) {
            bool match=a[i-1]==b[j-1];
            Cell diag={old[j-1].score+(match?2:-1),old[j-1].hits+(int)match};
            Cell del={old[j].score-2,old[j].hits};
            Cell ins={next[j-1].score-2,next[j-1].hits};
            Cell x=diag;
            if (better(del,x)) x=del;
            if (better(ins,x)) x=ins;
            next[j]=x;
        }
        if (better(next[m],best)) best=next[m];
        old.swap(next);
    }
    return best.hits;
}
extern "C" int align_score(const int* a, int n, const int* b, int m) {
    std::vector<Cell> old(m+1), next(m+1);
    for (int j=1;j<=m;j++) old[j]={-2*j,0};
    Cell best={-1000000000,0};
    for (int i=1;i<=n;i++) {
        next[0]={0,0};
        for (int j=1;j<=m;j++) {
            bool match=a[i-1]==b[j-1];
            Cell diag={old[j-1].score+(match?2:-1),old[j-1].hits+(int)match};
            Cell del={old[j].score-2,old[j].hits};
            Cell ins={next[j-1].score-2,next[j-1].hits};
            Cell x=diag;
            if (better(del,x)) x=del;
            if (better(ins,x)) x=ins;
            next[j]=x;
        }
        if (better(next[m],best)) best=next[m];
        old.swap(next);
    }
    return best.score;
}
extern "C" int local_hits(const int* a, int n, const int* b, int m) {
    std::vector<Cell> old(m+1), next(m+1);
    Cell best={0,0};
    for (int i=1;i<=n;i++) {
        next[0]={0,0};
        for (int j=1;j<=m;j++) {
            bool match=a[i-1]==b[j-1];
            Cell diag={old[j-1].score+(match?2:-1),old[j-1].hits+(int)match};
            Cell del={old[j].score-1,old[j].hits};
            Cell ins={next[j-1].score-1,next[j-1].hits};
            Cell x={0,0};
            if (better(diag,x)) x=diag;
            if (better(del,x)) x=del;
            if (better(ins,x)) x=ins;
            next[j]=x;
            if (better(x,best)) best=x;
        }
        old.swap(next);
    }
    return best.hits;
}
