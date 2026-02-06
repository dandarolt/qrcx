"""
QRC-X Examples and Tests
Demonstrates various use cases of the QRC-X encoding system
"""

from qrcx import QRCXEncoder, QRCXDecoder
import json


def example_basic():
    """Basic encoding and decoding example"""
    print("=" * 60)
    print("EXAMPLE 1: Basic Encoding")
    print("=" * 60)
    
    encoder = QRCXEncoder(size=32, error_correction=0.3)
    data = "QRC-X: Next-gen visual codes!"
    
    info = encoder.encode(data)
    print(f"Data: {data}")
    print(f"Compression: {info['compression_ratio']:.2f}x")
    encoder.save("example_basic.png", cell_size=12)
    print()


def example_with_metadata():
    """Encoding with metadata"""
    print("=" * 60)
    print("EXAMPLE 2: Encoding with Metadata")
    print("=" * 60)
    
    encoder = QRCXEncoder(size=48, error_correction=0.4)
    
    data = "Product Authentication Code: ABC-123-XYZ"
    metadata = {
        "product_id": "ABC-123-XYZ",
        "manufacturer": "TechCorp",
        "date": "2026-02-06",
        "batch": "B2026-001"
    }
    
    info = encoder.encode(data, metadata)
    print(f"Data: {data}")
    print(f"Metadata: {json.dumps(metadata, indent=2)}")
    print(f"Final size: {info['final_size']} bytes")
    encoder.save("example_metadata.png", cell_size=10)
    print()


def example_high_capacity():
    """High capacity encoding"""
    print("=" * 60)
    print("EXAMPLE 3: High Capacity Encoding")
    print("=" * 60)
    
    encoder = QRCXEncoder(size=128, error_correction=0.3)
    
    # Generate larger data
    data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 20
    
    info = encoder.encode(data)
    print(f"Data length: {len(data)} characters")
    print(f"Original size: {info['original_size']} bytes")
    print(f"Compressed size: {info['compressed_size']} bytes")
    print(f"Compression ratio: {info['compression_ratio']:.2f}x")
    print(f"Grid size: {info['grid_size']}x{info['grid_size']}")
    encoder.save("example_high_capacity.png", cell_size=6)
    print()


def example_error_correction_levels():
    """Different error correction levels"""
    print("=" * 60)
    print("EXAMPLE 4: Error Correction Levels")
    print("=" * 60)
    
    data = "Error correction test data"
    
    levels = [
        (0.3, "Low (30%) - Maximum capacity"),
        (0.5, "Medium (50%) - Balanced"),
        (0.7, "High (70%) - Maximum reliability")
    ]
    
    for level, description in levels:
        encoder = QRCXEncoder(size=48, error_correction=level)
        info = encoder.encode(data)
        filename = f"example_ec_{int(level*100)}.png"
        encoder.save(filename, cell_size=10)
        print(f"{description}")
        print(f"  Final size: {info['final_size']} bytes")
        print(f"  File: {filename}")
    print()


def example_url_encoding():
    """Encoding URLs"""
    print("=" * 60)
    print("EXAMPLE 5: URL Encoding")
    print("=" * 60)
    
    encoder = QRCXEncoder(size=48, error_correction=0.4)
    
    url = "https://github.com/dandarolt/qrcx"
    metadata = {
        "type": "url",
        "category": "repository",
        "created": "2026-02-06"
    }
    
    info = encoder.encode(url, metadata)
    print(f"URL: {url}")
    print(f"Signature: {info['signature'][:40]}...")
    encoder.save("example_url.png", cell_size=10)
    print()


def example_json_data():
    """Encoding JSON data"""
    print("=" * 60)
    print("EXAMPLE 6: JSON Data Encoding")
    print("=" * 60)
    
    encoder = QRCXEncoder(size=64, error_correction=0.4)
    
    json_data = {
        "user": "dandarolt",
        "project": "QRC-X",
        "version": "1.0.0",
        "features": ["multi-layer", "compression", "signatures"],
        "capacity": "64KB"
    }
    
    data_str = json.dumps(json_data)
    info = encoder.encode(data_str)
    
    print(f"JSON Data:")
    print(json.dumps(json_data, indent=2))
    print(f"\nCompression ratio: {info['compression_ratio']:.2f}x")
    encoder.save("example_json.png", cell_size=8)
    print()


def example_spectral_layer():
    """Demonstrating spectral layer"""
    print("=" * 60)
    print("EXAMPLE 7: Spectral Layer Visualization")
    print("=" * 60)
    
    encoder = QRCXEncoder(size=48, error_correction=0.4)
    
    data = "Secure authentication token: XYZ789"
    metadata = {"security_level": "high", "type": "auth_token"}
    
    encoder.encode(data, metadata)
    
    # Save without spectral
    encoder.save("example_no_spectral.png", cell_size=10, include_spectral=False)
    print("Saved without spectral layer: example_no_spectral.png")
    
    # Save with spectral
    encoder.save("example_with_spectral.png", cell_size=10, include_spectral=True)
    print("Saved with spectral layer: example_with_spectral.png")
    print()


def run_all_examples():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("QRC-X EXAMPLES SUITE")
    print("=" * 60 + "\n")
    
    example_basic()
    example_with_metadata()
    example_high_capacity()
    example_error_correction_levels()
    example_url_encoding()
    example_json_data()
    example_spectral_layer()
    
    print("=" * 60)
    print("ALL EXAMPLES COMPLETED!")
    print("=" * 60)
    print("\nGenerated files:")
    print("  - example_basic.png")
    print("  - example_metadata.png")
    print("  - example_high_capacity.png")
    print("  - example_ec_30.png, example_ec_50.png, example_ec_70.png")
    print("  - example_url.png")
    print("  - example_json.png")
    print("  - example_no_spectral.png, example_with_spectral.png")
    print()


if __name__ == "__main__":
    run_all_examples()
