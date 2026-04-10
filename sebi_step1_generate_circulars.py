"""
SEBI RAG Step 1 — Generate Synthetic SEBI Circulars
Creates 10 realistic SEBI circulars as text files
Saves to: sebi_circulars/ folder
"""

import os, json

os.makedirs("sebi_circulars", exist_ok=True)

G = "\033[92m"; W = "\033[0m"; BOLD = "\033[1m"

CIRCULARS = [
    {
        "id"      : "SEBI/HO/IVD/SEC2/CIR/2024/001",
        "date"    : "January 15, 2024",
        "subject" : "Amendment to SEBI (Prohibition of Insider Trading) Regulations — UPSI Definition and Trading Window",
        "filename": "sebi_circular_01_insider_trading.txt",
        "content" : """SECURITIES AND EXCHANGE BOARD OF INDIA
CIRCULAR — SEBI/HO/IVD/SEC2/CIR/2024/001
January 15, 2024

Subject: Amendment to SEBI (Prohibition of Insider Trading) Regulations, 2015 — Clarification on UPSI and Trading Window Closure

1. BACKGROUND
This circular is issued under Section 11(1) of SEBI Act, 1992. SEBI (Prohibition of Insider Trading) Regulations, 2015 prohibit trading in securities by insiders who possess UPSI.

2. DEFINITION OF UPSI
Unpublished Price Sensitive Information (UPSI) includes:
(a) Financial results — quarterly, half-yearly, and annual
(b) Dividends — interim and final
(c) Change in capital structure including buy-back, rights issue, bonus issue
(d) Mergers, acquisitions, demergers, amalgamations
(e) Major expansion plans or new projects
(f) Changes in key managerial personnel — MD, CEO, CFO, whole-time directors
(g) Material litigation where exposure exceeds 10% of net worth
Information ceases to be UPSI upon public disclosure through stock exchange filings.

3. TRADING WINDOW CLOSURE
The trading window shall be closed from the end of every quarter until 48 hours after declaration of financial results. For events in clause 2(c) through (g), trading window closes from board meeting date until 48 hours after public announcement. Designated persons shall not trade during closure irrespective of whether they possess UPSI.

4. STRUCTURED DIGITAL DATABASE (SDD)
Every listed company shall maintain SDD containing: names of persons who share UPSI, nature of UPSI shared, date of sharing, and purpose. SDD shall be preserved for minimum 8 years.

5. PRE-CLEARANCE REQUIREMENTS
Designated persons shall pre-clear trades above INR 10 lakh in any calendar quarter. Pre-clearance from Compliance Officer at least 2 trading days prior. Pre-cleared trades must execute within 7 trading days or fresh pre-clearance required.

6. PENALTIES
Violation may attract civil penalty up to INR 25 crore or 3 times profit made, criminal prosecution with imprisonment up to 10 years, and disgorgement of profits.

Issued under: SEBI Act 1992, Section 11(1)
"""
    },
    {
        "id"      : "SEBI/HO/MRD/DP/CIR/2024/002",
        "date"    : "February 3, 2024",
        "subject" : "Revised Framework for Futures and Options (F&O) Margin Requirements",
        "filename": "sebi_circular_02_fo_margins.txt",
        "content" : """SECURITIES AND EXCHANGE BOARD OF INDIA
CIRCULAR — SEBI/HO/MRD/DP/CIR/2024/002
February 3, 2024

Subject: Revised Framework for Futures and Options (F&O) Segment — Enhanced Margin Requirements and Position Limits

1. BACKGROUND
SEBI has reviewed the existing F&O margin framework to strengthen risk management and protect retail investors from excessive leverage. This circular supersedes SEBI/HO/MRD/DP/CIR/2022/045.

2. REVISED MARGIN REQUIREMENTS
SPAN Margin (Initial Margin):
- Minimum 15% of contract value for index derivatives
- Minimum 20% of contract value for stock derivatives

Exposure Margin:
- Index futures: 2% of contract value
- Stock futures: 5% of contract value or 1.5 standard deviations, whichever is higher

Extreme Loss Margin (ELM):
- Index derivatives: 3% of contract value
- Stock derivatives: Higher of 5% or 1.5 times standard deviation of daily logarithmic returns

3. POSITION LIMITS
Client Level: For index derivatives, gross open position shall not exceed 1% of free float market capitalisation. For stock derivatives, lower of 1% of free float market cap or INR 500 crore.
Trading Member Level: 15% of total open interest or INR 2,000 crore, whichever is lower.

4. INTRADAY MONITORING
Exchanges shall monitor margins on intraday basis. If margin falls below 75% of required level, member must replenish immediately. If not replenished within 60 minutes, exchange may initiate risk-reduction mode.

5. WEEKLY EXPIRY CONTRACTS
Only weekly expiry contracts of benchmark indices (Nifty 50, Sensex) shall be permitted. All other index option weekly contracts shall be discontinued. Minimum contract size for index derivatives shall be INR 15 lakh.

6. IMPLEMENTATION
Phase 1 (March 1, 2024): Revised SPAN and Exposure margins
Phase 2 (April 1, 2024): Revised position limits and weekly expiry restrictions
"""
    },
    {
        "id"      : "SEBI/HO/MRD/DRMNP/CIR/2024/003",
        "date"    : "March 10, 2024",
        "subject" : "Comprehensive Framework for Algorithmic Trading and Co-location Facilities",
        "filename": "sebi_circular_03_algo_trading.txt",
        "content" : """SECURITIES AND EXCHANGE BOARD OF INDIA
CIRCULAR — SEBI/HO/MRD/DRMNP/CIR/2024/003
March 10, 2024

Subject: Comprehensive Framework for Algorithmic Trading, High Frequency Trading (HFT) and Co-location Facilities

1. DEFINITION AND SCOPE
Algorithmic Trading means any order generated using automated execution logic where the decision to trade is taken by a computer program, order placement is automated, and no human intervention is required.
High Frequency Trading (HFT) is a subset of algorithmic trading characterised by high order-to-trade ratio, latency measured in microseconds, and holding period of less than one day.

2. APPROVAL REQUIREMENTS
All algorithms shall be approved by the stock exchange prior to deployment. Approval process includes logic review, simulation testing on exchange test environment, kill switch functionality verification, and risk parameter verification. Any material change to an approved algorithm requires fresh approval.

3. MANDATORY RISK CONTROLS
All algorithmic systems shall have: automated order-level risk checks, maximum order quantity limit, maximum order value limit per second, price band checks, cumulative daily loss limit, and automatic kill switch triggered at 70% of daily loss limit.

4. CO-LOCATION FACILITY
Stock exchanges offering co-location shall ensure equal latency for all subscribers, no preferential access to market data, and transparent pricing. A lottery system shall be used for allocation when demand exceeds supply.

5. ORDER-TO-TRADE RATIO
Maximum order-to-trade ratio: 100:1 for any trading session. Penalty for exceeding OTR: INR 1 lakh per violation per day.

6. AUDIT TRAIL
All algorithmic orders shall have a unique algo ID tag. Complete audit trail shall be maintained for 5 years.
"""
    },
    {
        "id"      : "SEBI/HO/CFD/CMD/CIR/2024/004",
        "date"    : "April 5, 2024",
        "subject" : "ESG Disclosure Requirements — Business Responsibility and Sustainability Report (BRSR)",
        "filename": "sebi_circular_04_esg_disclosure.txt",
        "content" : """SECURITIES AND EXCHANGE BOARD OF INDIA
CIRCULAR — SEBI/HO/CFD/CMD/CIR/2024/004
April 5, 2024

Subject: Enhanced ESG Disclosure Framework — BRSR Core and Third-Party Assurance Requirements

1. BRSR CORE — MANDATORY KPIs
Environment: GHG emissions (Scope 1, 2, 3), water consumption, energy consumption (renewable and non-renewable), waste generation and disposal.
Social: Employee diversity (gender, differently-abled), employee turnover rate, median wages for permanent employees, occupational health and safety incidents.
Governance: Transparency on complaints/grievances, cybersecurity incidents, anti-corruption policy compliance.

2. ASSURANCE REQUIREMENTS
Top 150 listed companies by market cap: Reasonable assurance on BRSR Core from FY 2023-24.
Top 250 listed companies: Limited assurance from FY 2024-25.
Top 500 listed companies: Limited assurance from FY 2025-26.
Top 1000 listed companies: Self-certification from FY 2023-24.

3. VALUE CHAIN DISCLOSURES
Listed companies shall disclose BRSR Core metrics for value chain partners contributing to 75% of purchases/sales by value.

4. PENALTIES
Non-disclosure attracts penalty under SEBI (LODR) Regulations. False disclosure attracts action under Section 15HA of SEBI Act.
"""
    },
    {
        "id"      : "SEBI/HO/IMD/IMD-II/CIR/2024/005",
        "date"    : "May 12, 2024",
        "subject" : "Revised Regulations for Mutual Funds — Risk-o-Meter, Expense Ratio and Direct Plan",
        "filename": "sebi_circular_05_mutual_funds.txt",
        "content" : """SECURITIES AND EXCHANGE BOARD OF INDIA
CIRCULAR — SEBI/HO/IMD/IMD-II/CIR/2024/005
May 12, 2024

Subject: Revised Framework for Mutual Funds — Risk-o-Meter Enhancement, Expense Ratio and Investor Protection

1. RISK-O-METER
Risk-o-Meter shall be updated from monthly to weekly basis for all open-ended mutual fund schemes. Risk levels: Low, Low to Moderate, Moderate, Moderately High, High, Very High. AMCs shall send SMS and email alerts whenever Risk-o-Meter changes.

2. EXPENSE RATIO — REVISED LIMITS FOR EQUITY SCHEMES
AUM up to INR 500 crore: Maximum 2.25%
AUM INR 500–750 crore: Maximum 2.00%
AUM INR 750–2,000 crore: Maximum 1.75%
AUM INR 2,000–5,000 crore: Maximum 1.60%
AUM above INR 5,000 crore: Maximum 1.05%
Debt schemes: TER limits 25 basis points lower than equity. Exit load shall not be charged in addition to TER.

3. DIRECT PLAN
Expense ratio of Direct Plan shall be lower than Regular Plan by at least the trail commission paid to distributors. AMCs shall prominently disclose the difference in returns between Direct and Regular plans.

4. PERFORMANCE BENCHMARKING
All mutual fund schemes shall be benchmarked against Total Return Index (TRI). Flexi-cap, Multi-cap, and Large & Mid Cap funds shall have two benchmarks.

5. SCHEME CATEGORISATION
AMCs can have only one scheme per category except: Index funds and ETFs, Fund of Funds, and Sectoral/Thematic funds.
"""
    },
    {
        "id"      : "SEBI/HO/CFD/DIL2/CIR/2024/006",
        "date"    : "June 20, 2024",
        "subject" : "Revised Guidelines for IPO and Draft Red Herring Prospectus (DRHP)",
        "filename": "sebi_circular_06_ipo_guidelines.txt",
        "content" : """SECURITIES AND EXCHANGE BOARD OF INDIA
CIRCULAR — SEBI/HO/CFD/DIL2/CIR/2024/006
June 20, 2024

Subject: Revised Guidelines for IPO, DRHP and Anchor Investor Framework

1. DRHP FILING
DRHP shall be filed simultaneously with SEBI and stock exchanges. DRHP shall be publicly available for 21 days for public comments. Issue size above INR 100 crore requires mandatory DRHP filing.

2. OBJECTS OF THE ISSUE
Companies shall disclose detailed utilisation plan with quarter-wise timeline, estimated costs, and monitoring agency for issues above INR 100 crore. General corporate purpose shall not exceed 25% of total issue size.

3. PROMOTER LOCK-IN
Minimum promoter contribution: 20% of post-issue paid-up capital.
Lock-in: Minimum promoter contribution locked for 18 months from allotment. Excess promoter holding locked for 6 months. Pre-IPO investors (holding >1 year): 6 months lock-in.

4. ANCHOR INVESTOR FRAMEWORK
Up to 60% of QIB portion can be allocated to anchor investors. Minimum application: INR 10 crore.
Lock-in: 50% of anchor allocation for 90 days, remaining 50% for 30 days.

5. PRICE BAND AND ALLOTMENT
Minimum price band spread: 105% of floor price. Price band disclosed at least 2 working days before opening.
Minimum allotment lot value: INR 15,000. Refund timeline: T+6 working days. Listing within T+6 working days.
"""
    },
    {
        "id"      : "SEBI/HO/CFD/CMD1/CIR/2024/007",
        "date"    : "July 8, 2024",
        "subject" : "Strengthening Framework for Related Party Transactions (RPT) for Listed Companies",
        "filename": "sebi_circular_07_related_party.txt",
        "content" : """SECURITIES AND EXCHANGE BOARD OF INDIA
CIRCULAR — SEBI/HO/CFD/CMD1/CIR/2024/007
July 8, 2024

Subject: Strengthening the Framework for Related Party Transactions (RPT) — Enhanced Disclosure and Shareholder Approval

1. DEFINITION OF RELATED PARTY
Related Party includes: promoter or promoter group entity, director or KMP and their relatives, subsidiary or associate companies, any entity over which promoter/director exercises significant influence (>20% voting rights).

2. MATERIAL RPT THRESHOLD
A transaction is material if: value exceeds INR 1,000 crore OR value exceeds 10% of annual consolidated turnover, whichever is lower. All material RPTs require shareholder approval through ordinary resolution. Related parties shall not vote on resolutions in which they are interested.

3. AUDIT COMMITTEE APPROVAL
All RPTs require prior Audit Committee approval. Omnibus approval for recurring transactions: maximum validity one financial year, shall specify maximum value and price formula.

4. DISCLOSURE REQUIREMENTS
Half-yearly disclosure to stock exchanges within 21 days of end of each half-year. Annual disclosure in Annual Report. Disclosures must include: name and relationship of related party, type and amount of transaction, terms including pricing policy, and justification.

5. ENHANCED REQUIREMENTS
For RPTs involving asset transfer: mandatory independent valuation report. For RPTs above INR 500 crore: mandatory fairness opinion from merchant banker.
"""
    },
    {
        "id"      : "SEBI/HO/MRD/TPD/CIR/2024/008",
        "date"    : "August 15, 2024",
        "subject" : "Cybersecurity and Cyber Resilience Framework (CSCRF) for SEBI Regulated Entities",
        "filename": "sebi_circular_08_cybersecurity.txt",
        "content" : """SECURITIES AND EXCHANGE BOARD OF INDIA
CIRCULAR — SEBI/HO/MRD/TPD/CIR/2024/008
August 15, 2024

Subject: Cybersecurity and Cyber Resilience Framework (CSCRF) for SEBI Regulated Entities

1. GOVERNANCE REQUIREMENTS
Market Infrastructure Institutions (MIIs) shall: constitute a Technology Committee of the Board, appoint CISO at Senior Management level, and report cybersecurity incidents to SEBI within 6 hours of detection. Other regulated entities (brokers, AMCs) shall appoint designated CISO and report incidents within 24 hours.

2. MANDATORY TECHNICAL CONTROLS
Multi-Factor Authentication (MFA) for all critical systems. End-to-end encryption for data in transit. Data encryption at rest for sensitive investor data. Privileged Access Management (PAM) solution. Security Information and Event Management (SIEM) system.

3. NETWORK SECURITY
Next-generation firewall. Intrusion Detection and Prevention System (IDS/IPS). DDoS protection. Network segmentation — DMZ, internal, and trading networks.

4. CYBER AUDIT
Annual comprehensive cyber audit by CERT-In empanelled auditor. Quarterly vulnerability assessment and penetration testing (VAPT). Audit reports submitted to SEBI within 30 days of completion.

5. INCIDENT RESPONSE
Entities shall maintain Cyber Incident Response Plan (CIRP). Minimum 2 cybersecurity drills per year. BCP for cyber incidents with RTO of 4 hours for critical systems.

6. DATA LOCALISATION
All trading data and investor data of Indian clients shall be stored within India. Cloud services for critical data shall use India-based data centres only.
"""
    },
    {
        "id"      : "SEBI/HO/AFD/AFD-II/CIR/2024/009",
        "date"    : "September 22, 2024",
        "subject" : "Revised Framework for Alternative Investment Funds (AIF) — Category I, II and III",
        "filename": "sebi_circular_09_aif.txt",
        "content" : """SECURITIES AND EXCHANGE BOARD OF INDIA
CIRCULAR — SEBI/HO/AFD/AFD-II/CIR/2024/009
September 22, 2024

Subject: Revised Framework for Alternative Investment Funds (AIF) — Enhanced Investor Protection and Disclosure

1. AIF CATEGORIES
Category I AIF: Invests in start-ups, early stage ventures, social ventures, SMEs, and infrastructure.
Category II AIF: Real estate funds, private equity funds, debt funds, fund of funds — no specific incentives.
Category III AIF: Employs diverse or complex trading strategies including listed or unlisted derivatives.

2. MINIMUM INVESTMENT AND CORPUS
Minimum investment per investor: INR 1 crore (employees/directors of AIF: INR 25 lakh). Minimum corpus of each scheme: INR 20 crore.

3. LEVERAGE LIMITS
Category I and II AIFs: No leverage except temporary funding needs not exceeding 30 days.
Category III AIFs: Maximum leverage of 2 times NAV. Open-ended Category III: Maximum 1.5 times NAV.

4. DISCLOSURE REQUIREMENTS
Quarterly report to investors within 60 days of end of quarter. Annual audited financial statements within 180 days of year end. Monthly portfolio disclosure for Category III.

5. VALUATION
All AIFs shall appoint independent valuer. Valuation policy shall be disclosed in Private Placement Memorandum (PPM). Category III AIFs investing in listed securities: mark-to-market valuation daily.

6. INVESTOR GRIEVANCE
All AIFs shall register on SEBI SCORES platform. Grievances shall be resolved within 21 working days.
"""
    },
    {
        "id"      : "SEBI/HO/MIRSD/SECFATF/CIR/2024/010",
        "date"    : "October 30, 2024",
        "subject" : "Enhanced KYC, AML and CFT Requirements for SEBI Registered Intermediaries",
        "filename": "sebi_circular_10_kyc_aml.txt",
        "content" : """SECURITIES AND EXCHANGE BOARD OF INDIA
CIRCULAR — SEBI/HO/MIRSD/SECFATF/CIR/2024/010
October 30, 2024

Subject: Enhanced KYC, AML and CFT Requirements for SEBI Registered Intermediaries

1. KYC REQUIREMENTS
Mandatory documents — Identity Proof: Aadhaar, PAN, Passport, Voter ID, Driving Licence. Address Proof: Aadhaar, utility bills (not older than 2 months), bank statement. PAN is mandatory for all market transactions.
Risk-based KYC: Low Risk — simplified KYC, Medium Risk — standard KYC, High Risk — Enhanced Due Diligence (EDD). Politically Exposed Persons (PEPs) classified as High Risk automatically.

2. BENEFICIAL OWNERSHIP
For non-individual clients, beneficial owner is the natural person who holds more than 25% shares, exercises control over management, or on whose behalf transaction is conducted. Identification of beneficial owner is mandatory.

3. TRANSACTION MONITORING
Intermediaries shall implement automated transaction monitoring systems. Suspicious Transaction Reports (STR) shall be filed with FIU-India within 7 days of suspicion. Cash Transaction Reports (CTR) for transactions above INR 10 lakh shall be filed monthly.

4. RECORD KEEPING
KYC records: maintained for 5 years after account closure. Transaction records: maintained for 5 years from transaction date.

5. PERIODIC KYC UPDATE
High Risk clients: update every 2 years. Medium Risk clients: update every 8 years. Low Risk clients: update every 10 years.

6. CENTRALISED KYC (CKYC)
All intermediaries shall upload KYC records to Central KYC Registry (CKYCR). CKYC number shall be used for all subsequent account openings.
"""
    },
]

def main():
    print(f"\n{BOLD}{'='*55}{W}")
    print(f"{BOLD}  SEBI RAG Step 1 — Generate Circulars{W}")
    print(f"{BOLD}{'='*55}{W}")
    index = []
    for c in CIRCULARS:
        path = os.path.join("sebi_circulars", c["filename"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(c["content"])
        index.append({"id":c["id"],"date":c["date"],"subject":c["subject"],"filename":c["filename"]})
        print(f"  {G}✓{W}  {c['filename']}")
    with open("sebi_circulars/index.json","w") as f:
        json.dump(index, f, indent=2)
    print(f"\n{BOLD}{G}  Step 1 COMPLETE! — 10 circulars generated{W}")
    print(f"  Next: python sebi_step2_build_rag.py\n")

if __name__ == "__main__":
    main()
