class swapTwoNumbers{
    public List<Integer> swapNumbers(int a, int b){
        List<Integer> list = new ArrayList<>();
        a = a^b;
        b = a^b;
        a = a^b;
        list.add(a);
        list.add(b);
        return list;
    }
}