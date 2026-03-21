    import seaborn as sns
    import matplotlib.pyplot as plt
    df = sns.load_dataset("tips")
    print(df.head())

    sns.set(style="whitegrid")

    sns.barplot(x='day', y='total_bill', data=df)
    plt.title("Average Total Bill per Day")
    plt.show()
    sns.lineplot(x='size', y='tip', data=df)
    plt.title("Tip by Size")
    plt.show()