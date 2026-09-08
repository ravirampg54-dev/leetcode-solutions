int countCommas(int n) {
    int res=0;
    for(int a=1;a<=n;++a)
    {
        if(a >=1000)
        {
            res+=1;
        }
    }
    return res;
}
