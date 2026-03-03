import pandas as pd

# 1. Create Sample Data (Simulating CSV imports)
ap_data = {
    'Invoice_ID': ['INV001', 'INV002', 'INV003', 'INV004'],
    'Vendor': ['Vendor_A', 'Vendor_B', 'Vendor_C', 'Vendor_D'],
    'AP_Amount': [1500.00, 2200.50, 3100.00, 450.00]
}

gl_data = {
    'Reference_ID': ['INV001', 'INV002', 'INV003', 'INV005'],
    'GL_Amount': [1500.00, 2100.50, 3100.00, 900.00]
}

df_ap = pd.DataFrame(ap_data)
df_gl = pd.DataFrame(gl_data)

# 2. Perform the Reconciliation (Outer Join)
recon = pd.merge(df_ap, df_gl, left_on='Invoice_ID', right_on='Reference_ID', how='outer')

# 3. Identify Discrepancies
recon['Variance'] = recon['AP_Amount'].fillna(0) - recon['GL_Amount'].fillna(0)
exceptions = recon[recon['Variance'] != 0]

print("--- Reconciliation Exceptions Identified ---")
print(exceptions[['Invoice_ID', 'Reference_ID', 'AP_Amount', 'GL_Amount', 'Variance']])

# 4. Export to Excel (For the Audit Trail)
# exceptions.to_excel("AP_GL_Exceptions_Report.xlsx", index=False)
