# investor360.py (Main Page)
import streamlit as st
import camelot
import tabula
import pdfplumber
import pandas as pd 

st.set_page_config(page_title="Investor360", layout="wide")
st.title("Investor360")
st.write("Welcome! Select a company from the sidebar to view its financials.")
import os

# List of companies
companies = [
    "ABANS ELECTRICALS PLC",
    "ABANS FINANCE PLC",
    "ACCESS ENGINEERING PLC",
    "ACL CABLES PLC",
    "ACL PLASTICS PLC",
    "ACME PRINTING & PACKAGING PLC",
    "AGALAWATTE PLANTATIONS PLC",
    "AGSTAR PLC",
    "AITKEN SPENCE HOTEL HOLDINGS PLC",
    "AITKEN SPENCE PLC",
    "ALLIANCE FINANCE COMPANY PLC",
    "ALPHA FIRE SERVICES PLC",
    "ALUMEX PLC",
    "AMANA BANK PLC",
    "AMANA TAKAFUL PLC",
    "AMANA TAKAFUL LIFE PLC",
    "AMBEON CAPITAL PLC",
    "AMBEON HOLDINGS PLC",
    "AMW CAPITAL LEASING AND FINANCE PLC",
    "ANILANA HOTELS AND PROPERTIES PLC",
    "ARPICO INSURANCE PLC",
    "ASIA ASSET FINANCE PLC",
    "ASIA CAPITAL PLC",
    "ASIA SIYAKA COMMODITIES LIMITED",
    "ASIAN HOTELS AND PROPERTIES PLC",
    "ASIRI SURGICAL HOSPITAL PLC",
    "ASIRI HOSPITAL HOLDINGS PLC",
    "ASSOCIATED MOTOR FINANCE COMPANY PLC",
    "Agarapatana Plantations PLC",
    "B P P L HOLDINGS PLC",
    "BAIRAHA FARMS PLC",
    "BALANGODA PLANTATIONS PLC", 
    "BANSEI ROYAL RESORTS HIKKADUWA PLC",
    "BERUWALA RESORTS PLC",
    "BIMPUTH LANKA INVESTMENTS PLC", 
    "BLUE DIAMONDS JEWELLERY WORLDWIDE PLC",
    "BOGALA GRAPHITE LANKA PLC",
    "BOGAWANTALAWA TEA ESTATES PLC", 
    "BROWN & COMPANY PLC",
    "BROWNS BEACH HOTELS PLC",
    "BROWNS INVESTMENTS PLC",
    "BUKIT DARAH PLC",
    "C M HOLDINGS PLC", 
    "C T HOLDINGS PLC",
    "C T LAND DEVELOPMENT PLC",
    "C. W. MACKIE PLC",
    "CABLE SOLUTIONS PLC", 
    "CAL FIVE YEAR CLOSED END FUND (“Units”)",
    "CAL FIVE YEAR OPTIMUM FUND (“Units”)",
    "CAPITAL ALLIANCE HOLDINGS PLC", 
    "CAPITAL ALLIANCE PLC",
    "CARGILLS (CEYLON) PLC",
    "CARGILLS BANK PLC",
    "CARGO BOAT DEVELOPMENT COMPANY PLC", 
    "CARSON CUMBERBATCH PLC",
    "CENTRAL FINANCE COMPANY PLC",
    "CENTRAL INDUSTRIES PLC",
    "CEYLINCO HOLDINGS PLC", 
    "CEYLON BEVERAGE HOLDINGS PLC",
    "CEYLON COLD STORES PLC",
    "CEYLON GRAIN ELEVATORS PLC", 
    "CEYLON GUARDIAN INVESTMENT TRUST PLC",
    "CEYLON HOSPITALS PLC",
    "CEYLON HOTELS CORPORATION PLC",
    "CEYLON INVESTMENT PLC",
    "CEYLON LAND & EQUITY PLC",
    "CEYLON TEA BROKERS PLC",
    "CEYLON TOBACCO COMPANY PLC",
    "CHEMANEX PLC",
    "CHEVRON LUBRICANTS LANKA PLC",
    "CHRISSWORLD PLC",
    "C I C HOLDINGS PLC",
    "CITIZENS DEVELOPMENT BUSINESS FINANCE PLC",
    "CITRUS LEISURE PLC",
    "CITY HOUSING & REAL ESTATE CO. PLC",
    "Co-operative Insurance Company PLC",
    "COLOMBO CITY HOLDINGS PLC",
    "COLOMBO DOCKYARD PLC",
    "COLOMBO FORT INVESTMENTS PLC",
    "COLOMBO INVESTMENT TRUST PLC",
    "COLOMBO LAND AND DEVELOPMENT COMPANY PLC",
    "COMMERCIAL BANK OF CEYLON PLC",
    "COMMERCIAL CREDIT AND FINANCE PLC",
    "COMMERCIAL DEVELOPMENT COMPANY PLC",
    "CONVENIENCE FOODS LANKA PLC",
    "DANKOTUWA PORCELAIN PLC",
    "DFCC BANK PLC",
    "DIALOG AXIATA PLC",
    "DIALOG FINANCE PLC",
    "DIESEL & MOTOR ENGINEERING PLC",
    "DIGITAL MOBILITY SOLUTIONS LANKA PLC",
    "DILMAH CEYLON TEA COMPANY PLC",
    "DIPPED PRODUCTS PLC",
    "DISTILLERIES COMPANY OF SRI LANKA PLC",
    "DOLPHIN HOTELS PLC",
    "E B CREASY & COMPANY PLC",
    "E M L CONSULTANTS PLC",
    "E - CHANNELLING PLC",
    "EAST WEST PROPERTIES PLC",
    "EASTERN MERCHANTS PLC",
    "EDEN HOTEL LANKA PLC",
    "ELPITIYA PLANTATIONS PLC",
    "EQUITY TWO PLC",
    "Ex-pack Corrugated Cartons PLC",
    "EXTERMINATORS PLC",
    "FIRST CAPITAL HOLDINGS PLC",
    "First Capital Treasuries PLC",
    "GALADARI HOTELS (LANKA) PLC",
    "GALLE FACE CAPITAL PARTNERS PLC",
    "GESTETNER OF CEYLON PLC",
    "GREENTECH ENERGY PLC",
    "HAPUGASTENNE PLANTATIONS PLC", 
    "HARISCHANDRA MILLS PLC",
    "HATTON NATIONAL BANK PLC",
    "HATTON PLANTATIONS PLC",
    "HAYCARB PLC", 
    "HAYLEYS FABRIC PLC",
    "HAYLEYS FIBRE PLC",
    "HAYLEYS LEISURE PLC",
    "HAYLEYS PLC",
    "HELA APPAREL HOLDINGS PLC", 
    "HEMAS HOLDINGS PLC",
    "HIKKADUWA BEACH RESORT PLC",
    "HNB ASSURANCE PLC",
    "HNB FINANCE PLC", 
    "HORANA PLANTATIONS PLC",
    "HOTEL SIGIRIYA PLC",
    "HOUSING DEVELOPMENT FINANCE CORPORATION BANK OF SL", 
    "hSenid Business Solutions PLC",
    "HUNAS HOLDINGS PLC",
    "HUNTER & COMPANY PLC",
    "HVA FOODS PLC", 
    "INDUSTRIAL ASPHALTS (CEYLON) PLC",
    "JANASHAKTHI FINANCE PLC",
    "JANASHAKTHI INSURANCE PLC",
    "JAT HOLDINGS PLC", 
    "JETWING SYMPHONY PLC",
    "JOHN KEELLS HOLDINGS PLC",
    "JOHN KEELLS HOTELS PLC",
    "JOHN KEELLS PLC", 
    "KAHAWATTE PLANTATIONS PLC",
    "KAPRUKA HOLDINGS PLC",
    "KEELLS FOOD PRODUCTS PLC",
    "KEGALLE PLANTATIONS PLC",
    "KELANI CABLES PLC",
    "KELANI TYRES PLC",
    "KELANI VALLEY PLANTATIONS PLC",
    "KELSEY DEVELOPMENTS PLC", 
    "KERNER HAUS GLOBAL SOLUTIONS PLC",
    "KOTAGALA PLANTATIONS PLC",
    "KOTMALE HOLDINGS PLC",
    "LB FINANCE PLC", 
    "LAKE HOUSE PRINTERS & PUBLISHERS PLC",
    "LANKA ALUMINIUM INDUSTRIES PLC",
    "LANKA ASHOK LEYLAND PLC", 
    "LANKA CERAMIC PLC",
    "LANKA CREDIT AND BUSINESS FINANCE PLC",
    "LANKA IOC PLC",
    "LANKA MILK FOODS (CWE) PLC", 
    "LANKA REALTY INVESTMENTS PLC",
    "LANKA TILES PLC",
    "LANKA VENTURES PLC",
    "LANKA WALLTILE PLC",
    "LANKEM CEYLON PLC", 
    "LANKEM DEVELOPMENTS PLC",
    "LAUGFS GAS PLC",
    "LAUGFS POWER PLC",
    "LAXAPANA PLC",
    "LEE HEDGES PLC", 
    "LION BREWERY (CEYLON) PLC",
    "LOLC FINANCE PLC",
    "LOLC GENERAL INSURANCE PLC",
    "L O L C HOLDINGS PLC", 
    "LOTUS HYDRO POWER PLC",
    "LUMINEX PLC",
    "L V L ENERGY FUND PLC",
    "MADULSIMA PLANTATIONS PLC", 
    "MAHARAJA FOODS PLC",
    "MAHAWELI COCONUT PLANTATIONS PLC",
    "MAHAWELI REACH HOTELS PLC", 
    "MALWATTE VALLEY PLANTATION PLC",
    "MARAWILA RESORTS PLC",
    "MASKELIYA PLANTATIONS PLC",
    "MELSTACORP PLC", 
    "MERCANTILE INVESTMENTS AND FINANCE PLC",
    "MERCANTILE SHIPPING COMPANY PLC", 
    "MERCHANT BANK OF SRI LANKA & FINANCE PLC",
    "MILLENNIUM HOUSING DEVELOPERS PLC",
    "MULLER & PHIPPS (CEYLON) PLC", 
    "MYLAND DEVELOPMENTS PLC",
    "NAMAL ACUITY VALUE FUND",
    "NAMUNUKULA PLANTATIONS PLC",
    "NATION LANKA FINANCE PLC", 
    "NATIONAL DEVELOPMENT BANK PLC",
    "NATIONS TRUST BANK PLC",
    "NAWALOKA HOSPITALS PLC",
    "ODEL PLC", 
    "OFFICE EQUIPMENT PLC",
    "ON'ALLY HOLDINGS PLC",
    "OVERSEAS REALTY (CEYLON) PLC",
    "PALM GARDEN HOTELS PLC", 
    "PAN ASIA BANKING CORPORATION PLC",
    "PANASIAN POWER PLC",
    "PARAGON CEYLON PLC",
    "PEGASUS HOTELS OF CEYLON PLC", 
    "PEOPLE'S INSURANCE PLC",
    "PEOPLE'S LEASING & FINANCE PLC",
    "PGP GLASS CEYLON PLC",
    "PMF FINANCE PLC", 
    "PRIME LANDS RESIDENCIES PLC",
    "PRINTCARE PLC",
    "R I L PROPERTY PLC",
    "RADIANT GEMS INTERNATIONAL PLC", 
    "RAIGAM WAYAMBA SALTERNS PLC",
    "RAMBODA FALLS PLC",
    "RENUKA AGRI FOODS PLC",
    "RENUKA CITY HOTELS PLC.", 
    "RENUKA FOODS PLC",
    "RENUKA HOLDINGS PLC",
    "RENUKA HOTELS PLC",
    "RESUS ENERGY PLC", 
    "RICHARD PIERIS AND COMPANY PLC",
    "RICHARD PIERIS EXPORTS PLC",
    "ROYAL CERAMICS LANKA PLC", 
    "ROYAL PALMS BEACH HOTELS PLC",
    "SAMPATH BANK PLC",
    "SAMSON INTERNATIONAL PLC",
    "SANASA DEVELOPMENT BANK PLC", 
    "SARVODAYA DEVELOPMENT FINANCE PLC",
    "SATHOSA MOTORS PLC",
    "SENFIN SECURITIES LIMITED", 
    "SENKADAGALA FINANCE COMPANY PLC",
    "SERENDIB HOTELS PLC",
    "SERENDIB LAND PLC",
    "SEYLAN BANK PLC", 
    "SEYLAN DEVELOPMENTS PLC",
    "SIERRA CABLES PLC",
    "SIGIRIYA VILLAGE HOTELS PLC",
    "SINGER (SRI LANKA) PLC", 
    "SINGER FINANCE LANKA PLC",
    "SINGHE HOSPITALS PLC",
    "SMB FINANCE PLC",
    "SOFTLOGIC CAPITAL PLC", 
    "SOFTLOGIC FINANCE PLC",
    "SOFTLOGIC HOLDINGS PLC",
    "SOFTLOGIC LIFE INSURANCE PLC",
    "SRI LANKA TELECOM PLC", 
    "STANDARD CAPITAL PLC",
    "SUNSHINE HOLDINGS PLC",
    "SWADESHI INDUSTRIAL WORKS PLC",
    "SWISSTEK (CEYLON) PLC", 
    "TAL LANKA HOTELS PLC",
    "TALAWAKELLE TEA ESTATES PLC",
    "TANGERINE BEACH HOTELS PLC",
    "TEA SMALLHOLDER FACTORIES PLC", 
    "TEEJAY LANKA PLC",
    "TESS AGRO PLC",
    "THE AUTODROME PLC",
    "THE COLOMBO FORT LAND AND BUILDING PLC", 
    "THE FORTRESS RESORTS PLC",
    "THE KANDY HOTELS COMPANY (1938) PLC",
    "THE KINGSBURY PLC", 
    "THE LANKA HOSPITALS CORPORATION PLC",
    "THE LIGHTHOUSE HOTEL PLC",
    "THE NUWARA ELIYA HOTELS COMPANY PLC", 
    "THREE ACRE FARMS PLC",
    "TOKYO CEMENT COMPANY (LANKA) PLC",
    "TRANS ASIA HOTELS PLC",
    "UB FINANCE PLC", 
    "UDAPUSSELLAWA PLANTATIONS PLC",
    "UNION ASSURANCE PLC",
    "UNION BANK OF COLOMBO PLC",
    "UNION CHEMICALS LANKA PLC", 
    "UNITED MOTORS LANKA PLC",
    "VALLIBEL FINANCE PLC",
    "VALLIBEL ONE PLC",
    "VALLIBEL POWER ERATHNA PLC", 
    "VIDULLANKA PLC"
]

# ------------------------------
# Sidebar selection
# ------------------------------
selected_company = st.sidebar.selectbox("Select a Company", companies)

# ------------------------------
# Display company info
# ------------------------------
st.header(selected_company)
st.write(f"Displaying financials for **{selected_company}**.")
 
import streamlit as st
import camelot
import pandas as pd

st.title("Investor 360 - PDF Table Extractor")

uploaded_file = st.file_uploader("Upload an Annual Report PDF", type="pdf")

if uploaded_file:
    pdf_path = "temp.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("PDF uploaded successfully!")

    st.subheader("Enter Page Numbers")
    col1, col2 = st.columns(2)
    with col1:
        income_from = st.number_input("Income Statement: From page", min_value=1, value=1)
        income_to = st.number_input("Income Statement: To page", min_value=income_from, value=income_from)
    with col2:
        balance_from = st.number_input("Balance Sheet: From page", min_value=1, value=1)
        balance_to = st.number_input("Balance Sheet: To page", min_value=balance_from, value=balance_from)

    if st.button("Extract Tables"):
        # Function to extract tables with Camelot only
        def extract_tables(pdf_path, page_from, page_to):
            combined_df = pd.DataFrame()
            for page in range(page_from, page_to + 1):
                tables = camelot.read_pdf(pdf_path, pages=str(page), flavor="lattice")
                if len(tables) == 0:
                    tables = camelot.read_pdf(pdf_path, pages=str(page), flavor="stream")
                for table in tables:
                    df = table.df
                    df["Page"] = page
                    combined_df = pd.concat([combined_df, df], ignore_index=True)
            return combined_df

        # Extract Income Statement
        df_inc = extract_tables(pdf_path, income_from, income_to)
        if not df_inc.empty:
            st.subheader("Income Statement")
            st.dataframe(df_inc, use_container_width=True)
            st.download_button("Download Income Statement CSV", df_inc.to_csv(index=False).encode("utf-8"), "income_statement.csv")
        else:
            st.warning("No tables found for Income Statement.")

        # Extract Balance Sheet
        df_bal = extract_tables(pdf_path, balance_from, balance_to)
        if not df_bal.empty:
            st.subheader("Balance Sheet")
            st.dataframe(df_bal, use_container_width=True)
            st.download_button("Download Balance Sheet CSV", df_bal.to_csv(index=False).encode("utf-8"), "balance_sheet.csv")
        else:
            st.warning("No tables found for Balance Sheet.")
