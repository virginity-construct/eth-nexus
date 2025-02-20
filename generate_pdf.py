from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        self.set_font('Arial', 'B', 24)
        self.set_text_color(0, 0, 0)
        self.cell(0, 20, 'ETH Nexus', 0, 1, 'C')
        self.set_font('Arial', 'I', 14)
        self.cell(0, 10, 'The Institutional Yield Layer for Ethereum', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_whitepaper():
    pdf = PDF()
    pdf.add_page()
    
    # Executive Summary
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Executive Summary', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, 'ETH Nexus bridges the gap between traditional finance and DeFi by providing institutional-grade yield generation strategies on Ethereum. Our platform enables sophisticated investors to access premium yields while maintaining the highest standards of security and risk management.')
    pdf.ln(10)

    # Market Overview
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Market Overview', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, 'The institutional DeFi market represents a $250B opportunity, with projected growth to $10T+ by 2030. ETH Nexus is positioned to capture this growth through our innovative yield strategies and institutional-grade infrastructure.')
    pdf.ln(10)

    # Yield Strategies
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Yield Strategies', 0, 1)
    
    strategies = [
        ('ETH Staking + EigenLayer', '5% - 12% APY', 'Secure, non-custodial staking with additional EigenLayer rewards.'),
        ('Institutional RWA Lending', '6% - 15% APY', 'Real-world asset-backed lending for institutional borrowers.'),
        ('Funding Rate Arbitrage', '10% - 30% APY', 'Automated cross-exchange funding rate capture strategies.'),
        ('ETH Options & Structured Vaults', '12% - 40% APY', 'Sophisticated options strategies for enhanced yield generation.'),
        ('MEV Yield Extraction', '25% - 50% APY', 'Advanced MEV capture through smart order routing.')
    ]

    for strategy, apy, description in strategies:
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, strategy, 0, 1)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, apy, 0, 1)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, description)
        pdf.ln(5)

    # Risk Management
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Risk Management', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, 'ETH Nexus employs sophisticated risk management protocols, including:\n\n- Real-time monitoring and automated risk adjustments\n- Multi-signature security protocols\n- Insurance coverage for smart contract risk\n- Regular third-party audits\n- Comprehensive compliance framework')
    pdf.ln(10)

    # Team & Partners
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Team & Partners', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, 'Our team combines decades of experience in traditional finance, DeFi, and blockchain technology. Strategic partnerships with leading institutions ensure best-in-class execution and risk management.')
    pdf.ln(10)

    # Contact Information
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Contact Information', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, 'For more information about ETH Nexus and our institutional yield strategies, please contact:\n\nEmail: info@ethnexus.com\nWebsite: https://ethnexus.com')

    # Save the PDF
    pdf.output('assets/ETH_Nexus_Whitepaper.pdf')

if __name__ == '__main__':
    create_whitepaper()
