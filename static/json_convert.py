import re
import json

ssim_pairs = []
with open('ssim_scores.txt') as f:
    for line in f:
        m = re.match(r"output_(\d+)\.wav <-> \1\.wav: SSIM = ([\d.]+)", line)
        if m:
            x, score = m.groups()
            ssim_pairs.append((int(x), float(score)))

# Sort descending by SSIM
ssim_pairs.sort(key=lambda x: -x[1])

# Save to JSON
with open('ssim_pairs.json', 'w') as f:
    json.dump(ssim_pairs, f)
