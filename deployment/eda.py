import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    # Disable deprecation warning for pyplot
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Read the cleaned data from 'data_raw.csv'
    data_clean = pd.read_csv('data.csv')

    # Application Title
    st.title("Data Visualization")

    # Sidebar to select a plot
    plot_selection = st.sidebar.selectbox("Please select a plot", ("Churn Distribution", "Country Distribution", "Churn by Gender in France", "Churn Rate by Age in France", "Churn by Product Number in France", "Churn by Active Membership in France", "Average Balance by Churn Status in France", "Churn by Credit Card Ownership in France"))

    # Plot 1: Churn Distribution
    if plot_selection == "Churn Distribution":
        st.subheader('Churn Distribution')
        churn_count = data_clean['churn'].sum()
        retention_count = data_clean['churn'].shape[0] - churn_count
        plt.bar(['Churn', 'Retention'], [churn_count, retention_count])
        plt.title('Churn distribution')
        st.pyplot()
        st.write("Churn:", churn_count)
        st.write("Retention:", retention_count)
        
        # Expander for Explanation Plot Churn Distribution
        with st.expander("Explanation Plot Churn Distribution"):
            st.caption("Terlihat bahwa customer retention lebih tinggi daripada customer churn. Namun tidak menutup kemungkinan bahwa kedepannya customer churn akan melebihi customer retention. Maka dari itu, kita akan melakukan visualisasi untuk menemukan pola apa yang berhubungan dari kolom-kolom yang ada dan mungkin saja menjadi alasan seorang customer untuk churn")

    # Plot 2: Country Distribution
    elif plot_selection == "Country Distribution":
        st.subheader('Country Distribution')
        country_counts = data_clean['country'].value_counts(normalize=True)
        labels = country_counts.index
        sizes = country_counts.values
        plt.pie(sizes, labels=labels, autopct='%.1f%%', startangle=90)
        plt.title('Countries')
        plt.axis('equal')
        st.pyplot()
        
        # Expander for Explanation Plot Country Distribution
        with st.expander("Explanation Plot Country Distribution"):
            st.caption("Negara yang memiliki persentase tertinggi untuk customer churn adalah France dengan nilai 50%. Maka dari itu, saya ingin melakukan analisis berdasarkan visualisasi data yang berfokus pada negara France")

    # Plot 3: Churn by Gender in France
    elif plot_selection == "Churn by Gender in France":
        st.subheader('Churn by Gender in France')
        data_france = data_clean[data_clean['country'] == 'France']
        data_france['churn_label'] = data_france['churn'].map({0: 'Loyal', 1: 'Churn'})
        plt.figure(figsize=(8, 4))
        sns.countplot(x='gender', hue='churn_label', data=data_france)
        plt.title('Churn by Gender in France')
        st.pyplot()
        
        # Expander for Explanation Plot Churn by Gender in France
        with st.expander("Explanation Plot Churn by Gender in France"):
            st.caption("Di negara France, untuk tingkat customer churn tertinggi ada pada gender Female. Dan tingkat customer loyal tertinggi ada pada gender Male.")


    # Plot 4: Churn Rate by Age in France
    elif plot_selection == "Churn Rate by Age in France":
        st.subheader('Churn Rate by Age in France')
        data_france = data_clean[data_clean['country'] == 'France']
        churn_by_age = data_france.groupby('age')['churn'].mean()
        plt.figure(figsize=(10, 6))
        plt.bar(churn_by_age.index, churn_by_age.values, color='skyblue')
        plt.xlabel('Age')
        plt.ylabel('Churn Rate')
        plt.title('Churn Rate by Age in France')
        plt.tight_layout()
        st.pyplot()
        
        # Expander for Explanation Plot Churn Rate by Age in France
        with st.expander("Explanation Plot Churn Rate by Age in France"):
            st.caption('Pada umur 40 tahun keatas, tingkat churn pada customer meningkat')    
                

    # Plot 5: Churn by Product Number in France
    elif plot_selection == "Churn by Product Number in France":
        st.subheader('Churn by Product Number in France')
        data_france = data_clean[data_clean['country'] == 'France']
        data_france['churn_label'] = data_france['churn'].map({0: 'Loyal', 1: 'Churn'})
        plt.figure(figsize=(8, 4))
        sns.countplot(x='products_number', hue='churn_label', data=data_france)
        plt.title('Churn by Product Number in France')
        st.pyplot()
        
        # Expander for Explanation Plot Churn Rate by Age in France
        with st.expander("Explanation Plot Churn by Product Number in France"):
            st.caption('Produk nomor 4 adalah produk yang sepi peminat. Produk 2 adalah produk yang berpotensi meningkatkan retention customer atau keloyalan customer sedangkan produk nomor 1 adalah produk yang berpotensi terhadap tingkat churn pada customer.')
        

    # Plot 6: Churn by Active Membership in France
    elif plot_selection == "Churn by Active Membership in France":
        st.subheader('Churn by Active Membership in France')
        data_france = data_clean[data_clean['country'] == 'France']
        data_france['churn_label'] = data_france['churn'].map({0: 'Loyal', 1: 'Churn'})
        data_france['active_member'] = data_france['active_member'].map({0: 'Pasif', 1: 'Aktif'})
        plt.figure(figsize=(8, 4))
        sns.countplot(x='active_member', hue='churn_label', data=data_france)
        plt.title('Churn by Active Membership in France')
        st.pyplot()
    
        # Expander for Explanation Plot Churn by Active Membership in France
        with st.expander("Explanation Plot Churn by Active Membership in France"):
            st.caption('Tingkat churn disebabkan juga oleh customer yang pasif untuk menggunakan layanan, karena customer tersebut pasif maka memperbesar peluang untuk churn atau keluar dari status nasabah nya.')


    # Plot 7: Average Balance by Churn Status in France
    elif plot_selection == "Average Balance by Churn Status in France":
        st.subheader('Average Balance by Churn Status in France')
        data_france = data_clean[data_clean['country'] == 'France']
        data_france['churn_label'] = data_france['churn'].map({0: 'Loyal', 1: 'Churn'})
        mean_balance = data_france.groupby('churn_label')['balance'].mean().reset_index()
        plt.figure(figsize=(8, 6))
        sns.barplot(x='churn_label', y='balance', data=mean_balance)
        plt.title('Average Balance by Churn Status in France')
        plt.xlabel('Churn Status')
        plt.ylabel('Average Balance')
        st.pyplot()
        
        # Expander for Explanation Plot Average Balance by Churn Status in France
        with st.expander("Explanation Plot Average Balance by Churn Status in France"):
             st.caption('Rata-rata saldo pada customer churn lebih tinggi dibandingkan customer yang loyal. Maka dari itu, kita sebagai pihak bank wajib untuk mengurangi tingkat churn customer, karena apabila tingkat churn semakin tinggi maka semakin besar atau timpang rata-rata saldo customer churn dibandingkan customer loyal dan hal itu dapat menyebabkan bank merugi.')
       

    # Plot 8: Churn by Credit Card Ownership in France
    elif plot_selection == "Churn by Credit Card Ownership in France":
        st.subheader('Churn by Credit Card Ownership in France')
        data_france = data_clean[data_clean['country'] == 'France']
        data_france['churn_label'] = data_france['churn'].map({0: 'Loyal', 1: 'Churn'})
        plt.figure(figsize=(8, 4))
        sns.countplot(x='credit_card', hue='churn_label', data=data_france)
        plt.title('Churn by Credit Card Ownership in France')
        st.pyplot()
        
        # Expander for Explanation Plot Churn by Credit Card Ownership in France
        with st.expander("Explanation Plot Churn by Credit Card Ownership in France"):
            st.caption('Customer yang mempunyai kartu kredit mayoritas adalah customer loyal dan customer yang churn juga. Hanya ada sedikit customer yang tidak mempunyai kartu kredit, karena mayoritas customer sudah mempunyai kartu kredit')
