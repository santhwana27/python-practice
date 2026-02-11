import statistics as st

def show_stats(a):
    print("Sum =", sum(a))
    print("Mean =", st.mean(a))
    print("Median =", st.median(a))
    print("Variance =", st.pvariance(a))

numbers = list(map(int, input("Enter numbers: ").split()))
show_stats(numbers)


