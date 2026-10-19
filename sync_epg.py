import os, urllib.request, gzip, xml.etree.ElementTree as ET, pathlib
url = os.environ['EPG_SOURCE_URL']
req = urllib.request.Request(url, headers={'User-Agent':'EZSport-EPG-Sync/1.0'})
with urllib.request.urlopen(req, timeout=120) as response:
    raw = response.read(100 * 1024 * 1024 + 1)
if len(raw) > 100 * 1024 * 1024:
    raise ValueError('EPG source too large')
xml = gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw
root = ET.fromstring(xml)
if root.tag != 'tv' or not root.findall('channel') or not root.findall('programme'):
    raise ValueError('Invalid XMLTV or no channels/programmes; refusing update')
out = pathlib.Path('epg.xml.gz')
with gzip.open(out, 'wb', compresslevel=6) as f:
    f.write(xml)
print(f'Validated {len(root.findall("channel"))} channels, {len(root.findall("programme"))} programmes, wrote {out.stat().st_size} bytes')
