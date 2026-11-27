import json
import math
import html

def generate_vosviewer_svg():
    with open('data/vosviewer/luan_an_real_network.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    items = data['network']['items']
    links = data['network']['links']

    # Canvas dimensions
    width = 1280
    height = 840
    padding_x = 100
    padding_y = 120

    # Cluster styling
    # Cluster 1: AI / Stimulus (Rose/Red)
    # Cluster 2: Organism / E-Satisfaction (Emerald/Green)
    # Cluster 3: Response / Impulse Buying (Blue)
    # Cluster 4: Boundary / Ego Depletion & Self-Regulation (Amber/Orange)
    cluster_meta = {
        1: {"name": "Cluster 1: Algorithmic Stimuli (S)", "color": "#e11d48", "bg": "#ffe4e6", "border": "#be123c"},
        2: {"name": "Cluster 2: Experiential Organism (O)", "color": "#059669", "bg": "#d1fae5", "border": "#047857"},
        3: {"name": "Cluster 3: Behavioral Response (R)", "color": "#2563eb", "bg": "#dbeafe", "border": "#1d4ed8"},
        4: {"name": "Cluster 4: Boundary & Self-Control (M)", "color": "#d97706", "bg": "#fef3c7", "border": "#b45309"}
    }

    # Normalize coordinates from [-0.95, 0.95] to canvas [padding_x, width - padding_x]
    # In VOSviewer, y is often inverted (up is positive), let's ensure standard Cartesian mapping
    plot_w = width - 2 * padding_x
    plot_h = height - 2 * padding_y - 60 # room for header and legend

    center_x = width / 2
    center_y = (height - 60) / 2 + 30

    node_dict = {}
    for it in items:
        # Scale coords
        nx = center_x + it['x'] * (plot_w / 2.1)
        ny = center_y + it['y'] * (plot_h / 2.1)
        occ = it['weights']['Occurrences']
        radius = 8 + math.sqrt(occ) * 1.55 # radius between ~15 and 38px
        node_dict[it['id']] = {
            "id": it['id'],
            "label": it['label'],
            "x": nx,
            "y": ny,
            "occ": occ,
            "links": it['weights']['Links'],
            "cluster": it['cluster'],
            "radius": radius
        }

    svg_parts = []
    svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="font-family:'Plus Jakarta Sans',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; background:#ffffff;">
  <defs>
    <filter id="nodeShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
    <filter id="pillShadow" x="-10%" y="-15%" width="120%" height="130%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Title & Software Banner -->
  <rect x="25" y="18" width="{width-50}" height="56" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="45" y="44" font-size="14" font-weight="800" fill="#0f172a" letter-spacing="0.5">FIGURE 2: EMPIRICAL BIBLIOMETRIC CO-OCCURRENCE NETWORK MAP (VOSVIEWER ANALYSIS)</text>
  <text x="45" y="62" font-size="10.5" fill="#64748b">Corpus: N = 1,441 core studies (2014–2024) | Fractional Counting | Min. Occurrence threshold T = 5 | Total Links: 250</text>
  <rect x="{width-215}" y="28" width="175" height="34" rx="6" fill="#ffffff" stroke="#94a3b8"/>
  <text x="{width-128}" y="50" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">VOSviewer v1.6.20 Output</text>

  <!-- Network Canvas Border -->
  <rect x="25" y="86" width="{width-50}" height="{height-170}" rx="10" fill="#fafafa" stroke="#e2e8f0" stroke-width="1.5"/>
''')

    # 1. Draw Links
    svg_parts.append('  <!-- Co-occurrence Links (250 edges) -->\n  <g id="network-links">')
    for link in links:
        src = node_dict.get(link['source_id'])
        tgt = node_dict.get(link['target_id'])
        if not src or not tgt:
            continue
        strength = link.get('strength', 1)
        # Stroke width proportional to strength
        sw = max(0.6, min(4.2, strength * 0.16))
        # Opacity
        opacity = max(0.12, min(0.65, strength * 0.035))
        # Color: if same cluster, match cluster tint; else subtle slate
        if src['cluster'] == tgt['cluster']:
            stroke_color = cluster_meta.get(src['cluster'], {}).get('color', '#94a3b8')
        else:
            stroke_color = "#94a3b8"

        svg_parts.append(f'    <line x1="{src["x"]:.1f}" y1="{src["y"]:.1f}" x2="{tgt["x"]:.1f}" y2="{tgt["y"]:.1f}" stroke="{stroke_color}" stroke-width="{sw:.2f}" stroke-opacity="{opacity:.2f}"/>')
    svg_parts.append('  </g>\n')

    # 2. Draw Nodes (Circles)
    svg_parts.append('  <!-- Network Nodes (28 keywords) -->\n  <g id="network-nodes">')
    for nid, node in sorted(node_dict.items(), key=lambda x: x[1]['occ']):
        cm = cluster_meta.get(node['cluster'], {"color": "#64748b", "bg": "#f1f5f9", "border": "#475569"})
        svg_parts.append(f'''    <circle cx="{node['x']:.1f}" cy="{node['y']:.1f}" r="{node['radius']:.1f}" fill="{cm['color']}" stroke="#ffffff" stroke-width="2.5" filter="url(#nodeShadow)" fill-opacity="0.88">
      <title>{html.escape(node['label'])} (Occurrences: {node['occ']}, Links: {node['links']})</title>
    </circle>''')
    svg_parts.append('  </g>\n')

    # 3. Draw Node Labels (with white pill background for readability like VOSviewer)
    svg_parts.append('  <!-- Node Labels with high-contrast badge -->\n  <g id="node-labels">')
    for nid, node in sorted(node_dict.items(), key=lambda x: x[1]['occ'], reverse=True):
        cm = cluster_meta.get(node['cluster'], {"color": "#0f172a"})
        label = node['label']
        fs = max(9.5, min(14.0, 8.5 + math.sqrt(node['occ']) * 0.35))
        fw = "800" if node['occ'] > 150 else ("700" if node['occ'] > 70 else "600")
        label_len = len(label)
        badge_w = label_len * (fs * 0.58) + 12
        badge_h = fs + 8
        bx = node['x'] - badge_w / 2
        by = node['y'] + node['radius'] + 4
        # If too close to bottom of canvas, place label above
        if by + badge_h > height - 100:
            by = node['y'] - node['radius'] - badge_h - 4

        svg_parts.append(f'''    <rect x="{bx:.1f}" y="{by:.1f}" width="{badge_w:.1f}" height="{badge_h:.1f}" rx="4" fill="#ffffff" stroke="{cm['color']}" stroke-width="1.2" stroke-opacity="0.5" filter="url(#pillShadow)"/>
    <text x="{node['x']:.1f}" y="{by + fs + 1:.1f}" text-anchor="middle" font-size="{fs:.1f}" font-weight="{fw}" fill="{cm['color']}">{html.escape(label)}</text>''')
    svg_parts.append('  </g>\n')

    # 4. Legend Footer (4 Clusters)
    svg_parts.append(f'''  <!-- Legend Footer -->
  <g id="legend-footer" transform="translate(25, {height - 72})">
    <rect x="0" y="0" width="{width - 50}" height="58" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
    <text x="20" y="24" font-size="11" font-weight="800" fill="#0f172a">VOSVIEWER THEMATIC CLUSTERS:</text>
''')

    col_w = (width - 70) / 4
    x_positions = [20, 20 + col_w, 20 + 2 * col_w, 20 + 3 * col_w]

    cluster_descriptions = [
        (1, "Cluster 1: Stimulus (AI/PP/ACC)", "348 articles | Algorithmic Cues"),
        (2, "Cluster 2: Organism (Satisfaction/Trust)", "174 articles | Internal Evaluation"),
        (3, "Cluster 3: Response (Impulse Buying/UBI)", "344 articles | Behavioral Checkout"),
        (4, "Cluster 4: Boundary (Ego Depletion/Control)", "62 articles | Regulatory Friction")
    ]

    for idx, (cid, title, sub) in enumerate(cluster_descriptions):
        cm = cluster_meta[cid]
        col_x = x_positions[idx]
        svg_parts.append(f'''    <g transform="translate({col_x}, 12)">
      <circle cx="10" cy="18" r="7" fill="{cm['color']}" stroke="#ffffff" stroke-width="1.5"/>
      <text x="24" y="16" font-size="10.5" font-weight="800" fill="{cm['color']}">{title}</text>
      <text x="24" y="29" font-size="9" fill="#64748b">{sub}</text>
    </g>''')

    svg_parts.append('''  </g>
</svg>''')

    full_svg = "\n".join(svg_parts)

    with open('lab_projects/figures/figure2_vosviewer_real_network.svg', 'w', encoding='utf-8') as f:
        f.write(full_svg)
    print(f"Generated lab_projects/figures/figure2_vosviewer_real_network.svg ({len(full_svg)} bytes)")

if __name__ == '__main__':
    generate_vosviewer_svg()
