# Credit-Card-Fraud-Detection
## Overview of the Problem

The addressed problem consists of analyzing and detecting possible fraudulent credit card transactions in order to assist customers in avoiding unauthorized charges for purchases they did not make. This is a highly relevant issue, especially due to the rise of virtual banks (such as PayPal, Nubank, and other), where there are many complaints and discussions about banking fraud on the internet, with little assistance provided by banks to their customers. This lack of support results in low trust and loss of public confidence.

To tackle this problem, we employed Semi-Supervised Learning to study the issue and utilized One-Class Classification to find a way to detect these frauds before customers are charged for unauthorized purchases they did not make. These techniques are highly relevant as they can also leverage unlabeled data for prediction and classification tasks.

In the real world, it is notably easier to find unlabeled data, especially in specific contexts such as text analysis. Additionally, unlabeled data tends to be cheaper and easier to collect compared to labeled data. This phenomenon occurs because unlabeled data can be readily collected through automated scraping tools. This technique is known as *data scraping*. The ease of collecting unlabeled data is due to the fact that labeled examples mostly require human interaction, often involving experts to perform the labeling task.

To better explain the group's motivation in choosing the dataset, it is necessary to understand what will be analyzed. In this work, we chose to analyze *point anomalies*, which refer to individual data points that are considered abnormal in relation to other data points in the dataset. In the image below, for example, $O_1, O_2$, and $O_3$ are considered abnormal data points compared to the data points within the normal regions $N_1$ and $N_2$.

![image](https://github.com/julianafalves/Credit-Card-Fraud-Detection/assets/49698966/880ef261-8627-4c6c-b5ec-df8f0ac00a88)


Based on this information, we selected the dataset [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) to study and gain a better understanding of how machine learning algorithms can be used for anomaly detection. In this case, an anomaly occurs when there is a transaction from the same customer that deviates from the normal usage patterns of the credit card. For example, suppose a person X has an average monthly spending of 1000 reais on their credit card. If, by chance, they exceed this average by making a transaction significantly higher than their usual spending, the algorithm will detect and classify it as an anomaly.

The dataset contains transactions that occurred over a span of two days, during which there were 492 frauds out of 284,807 transactions, accounting for 0.17% of all transactions within that time frame. To facilitate the analysis, the dataset only includes numerical data resulting from Principal Component Analysis (PCA) transformation. However, due to privacy and security concerns, no further information about the features V1, V2, V3, ..., V28 could be obtained, except that they represent the main components obtained after PCA. The only two pieces of information that were not transformed are 'Time', which represents the seconds elapsed between each transaction after the first transaction in the dataset, and 'Amount', which denotes the value of the transaction.

The class that distinguishes between normal and anomalous transactions is divided into 0 and 1, respectively.
