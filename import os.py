import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# 1. Cấu hình thông tin Key Vault từ hình ảnh của bạn
key_vault_name = "asmtrangkv"
kv_uri = f"https://{key_vault_name}.vault.azure.net"
secret_name = "bimat"

def get_azure_secret():
    try:
        # 2. Khởi tạo phương thức xác thực
        credential = DefaultAzureCredential()
        
        # 3. Kết nối tới Secret Client
        client = SecretClient(vault_url=kv_uri, credential=credential)

        # 4. Lấy giá trị của secret 'bimat'
        retrieved_secret = client.get_secret(secret_name)
        
        print(f"Kết nối thành công!")
        print(f"Giá trị bí mật của '{secret_name}' là: {retrieved_secret.value}")
        return retrieved_secret.value

    except Exception as e:
        print(f"Lỗi rồi Tuấn ơi: {e}")

if __name__ == "__main__":
    get_azure_secret()