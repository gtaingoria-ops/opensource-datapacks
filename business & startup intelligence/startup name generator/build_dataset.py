import json
import random

# 1. RAW DATA LISTS (Expand these lists to reach even higher numbers)
# We use compact lists here to save space, then the script expands them into objects.

prefixes_raw = [
    "aero", "alfa", "algo", "alt", "ambi", "apex", "arch", "astro", "auto", "avi", "azure", 
    "bio", "bit", "block", "blue", "bolt", "bright", "byte", "cap", "cell", "cent", "chrono", 
    "cipher", "clear", "cloud", "code", "cogni", "core", "crypt", "cyber", "data", "deep", 
    "digi", "dock", "dual", "dyn", "echo", "eco", "edge", "elites", "ember", "equi", "ether", 
    "euro", "ever", "exo", "fast", "fin", "first", "flash", "flex", "flow", "flux", "force", 
    "front", "fubi", "fuse", "futur", "gate", "gen", "geo", "giga", "glo", "go", "gold", 
    "green", "grid", "gro", "halo", "hash", "hex", "high", "holo", "hub", "hyper", "idea", 
    "igni", "in", "inf", "inno", "inter", "intra", "iron", "iso", "jet", "key", "kin", 
    "launch", "lib", "life", "light", "link", "logic", "lumen", "lunar", "macro", "magna", 
    "main", "max", "mech", "mega", "meta", "metri", "micro", "mind", "mobi", "mod", "mono", 
    "moon", "morph", "motion", "my", "nano", "nav", "neo", "net", "neur", "next", "nex", 
    "node", "nomad", "nova", "nu", "nuke", "null", "octa", "omni", "on", "one", "open", 
    "opti", "orbit", "out", "over", "pan", "para", "path", "pay", "peak", "peer", "penta", 
    "per", "pet", "phase", "phoenix", "photon", "pico", "pixel", "plan", "plas", "play", 
    "plex", "plus", "poly", "port", "power", "prime", "prism", "pro", "proto", "pulse", 
    "pure", "pyro", "quad", "quant", "quest", "quick", "radi", "rapid", "ray", "real", 
    "red", "retro", "re", "rise", "robo", "rocket", "root", "safe", "scale", "scope", 
    "secure", "sense", "servo", "shift", "shop", "sigma", "signal", "silver", "simple", 
    "sky", "smart", "snap", "soft", "solar", "solid", "solo", "sonic", "source", "space", 
    "spark", "spect", "speed", "sphere", "spin", "spot", "spring", "stack", "star", "stat", 
    "steam", "steel", "stellar", "strat", "stream", "structure", "studio", "sum", "sun", 
    "super", "sure", "switch", "sym", "syn", "sys", "tag", "tech", "tele", "terra", 
    "tether", "think", "time", "top", "total", "touch", "trace", "trans", "tri", "true", 
    "trust", "turbo", "twin", "uber", "ultra", "uni", "up", "urb", "val", "vapor", "vari", 
    "velo", "vent", "ver", "via", "vibe", "video", "view", "virtu", "vis", "vital", "viv", 
    "voice", "volt", "vortex", "vox", "warp", "wave", "web", "west", "wide", "wise", 
    "wolf", "xeno", "yard", "zen", "zero", "zeta", "zone", "zoom"
]

roots_raw = [
    "academy", "access", "action", "active", "actor", "ad", "add", "admin", "advis", 
    "agent", "ai", "aid", "aim", "air", "alert", "alley", "alpha", "amp", "analys", 
    "anchor", "angle", "answer", "ant", "app", "arc", "area", "arena", "arm", "array", 
    "art", "ask", "asset", "assist", "atom", "audit", "aura", "auto", "av", "avenue", 
    "avi", "axis", "b", "back", "badge", "balance", "ball", "band", "bank", "bar", 
    "base", "basket", "bat", "bay", "beam", "bear", "beat", "bee", "bell", "bench", 
    "beta", "bid", "bike", "bill", "bin", "bio", "bit", "bite", "black", "blade", 
    "blend", "block", "blog", "blue", "board", "boat", "body", "bolt", "bond", "book", 
    "boost", "boot", "bot", "box", "brain", "brand", "bridge", "bright", "bro", "buddy", 
    "buffer", "bug", "build", "bulb", "bull", "bunker", "burst", "bus", "buy", "buzz", 
    "byte", "c", "cab", "cache", "cad", "cage", "calc", "call", "cam", "camp", "can", 
    "cap", "capital", "car", "card", "care", "cargo", "cart", "case", "cash", "cast", 
    "cat", "catch", "cell", "center", "central", "chain", "champ", "channel", "chap", 
    "charge", "chart", "chat", "check", "chef", "chip", "choice", "city", "claim", "clan", 
    "class", "clean", "click", "client", "clip", "clock", "cloud", "club", "cluster", 
    "coach", "coast", "coat", "code", "coin", "collab", "color", "com", "comb", "command", 
    "connect", "console", "construct", "consult", "contact", "content", "control", "cook", 
    "cool", "cop", "core", "corner", "corp", "cost", "count", "course", "cover", "craft", 
    "crate", "credit", "crew", "cross", "crowd", "crown", "cruise", "crypto", "cube", 
    "cult", "cure", "current", "curve", "cut", "cycle", "d", "dad", "daily", "dairy", 
    "dam", "dance", "dark", "dash", "data", "date", "day", "deal", "deck", "deep", 
    "define", "deliv", "delta", "demo", "den", "design", "desk", "dev", "dial", "dice", 
    "diet", "dig", "digit", "dine", "direct", "dish", "disk", "display", "div", "doc", 
    "dock", "dog", "domain", "dome", "door", "dot", "draft", "drag", "drain", "draw", 
    "dream", "drift", "drill", "drink", "drive", "drop", "drum", "dry", "dual", "duck", 
    "due", "duo", "dust", "duty", "e", "eagle", "ear", "earth", "ease", "east", "eat", 
    "echo", "edge", "edit", "edu", "effect", "egg", "ego", "eight", "elastic", "electric", 
    "element", "elite", "email", "ember", "empire", "engine", "enter", "entry", "env", 
    "epic", "epoch", "equal", "equip", "equity", "era", "error", "estate", "ether", "euro", 
    "event", "ever", "evo", "ex", "exam", "exec", "exit", "expert", "export", "express", 
    "eye", "f", "face", "fact", "factor", "factory", "fair", "fan", "farm", "fast", "fat", 
    "feed", "feel", "fence", "field", "file", "fill", "film", "filter", "fin", "find", 
    "fine", "fire", "firm", "first", "fish", "fit", "fix", "flag", "flash", "flat", 
    "fleet", "flex", "flight", "flip", "float", "floor", "flow", "flower", "fluid", 
    "flux", "fly", "focus", "fog", "fold", "folk", "folio", "food", "foot", "force", 
    "forge", "form", "fort", "forum", "forward", "found", "fox", "frame", "free", "fresh", 
    "friend", "front", "fruit", "fuel", "full", "fun", "fund", "fuse", "fusion", "future", 
    "g", "gain", "galaxy", "gallery", "game", "gap", "garage", "garden", "gas", "gate", 
    "gather", "gauge", "gear", "geek", "gem", "gen", "general", "genius", "geo", "get", 
    "ghost", "giant", "gift", "gig", "glass", "glide", "global", "globe", "glow", "go", 
    "goal", "goat", "gold", "golf", "good", "goods", "goose", "gopher", "grade", "gram", 
    "grand", "graph", "grass", "gravity", "gray", "great", "green", "grid", "grill", 
    "grip", "ground", "group", "grow", "guard", "guess", "guest", "guide", "guild", 
    "guru", "gym", "h", "habit", "hack", "hair", "hall", "halo", "hammer", "hand", 
    "handle", "hang", "harbor", "hard", "hash", "hat", "hatch", "haven", "hawk", "head", 
    "health", "heart", "heat", "heavy", "hedge", "hello", "help", "hero", "hex", "hi", 
    "hide", "high", "hike", "hill", "hint", "hip", "hire", "hit", "hive", "hobby", 
    "hold", "hole", "home", "honey", "hook", "hop", "hope", "horizon", "horn", "host", 
    "hotel", "hour", "house", "hub", "human", "hunt", "hut", "hydro", "hyper", "i", 
    "ice", "icon", "idea", "ident", "ignite", "image", "impact", "import", "impulse", 
    "in", "inc", "index", "indigo", "info", "infra", "ink", "inn", "input", "insight", 
    "inspect", "instant", "intel", "inter", "invest", "ion", "iris", "iron", "island", 
    "item", "j", "jack", "jam", "jar", "java", "jaw", "jay", "jazz", "jet", "jewel", 
    "job", "jockey", "join", "joint", "jolt", "journal", "journey", "joy", "judge", 
    "jug", "juice", "jump", "junction", "jungle", "junior", "junk", "jury", "just", 
    "k", "karma", "keep", "key", "kick", "kid", "kill", "kin", "kind", "king", "kit", 
    "kite", "knight", "knit", "knock", "knot", "know", "koala", "l", "lab", "label", 
    "labor", "lace", "ladder", "ladle", "lady", "lake", "lamp", "land", "lane", "lap", 
    "laser", "last", "latch", "late", "launch", "lava", "law", "layer", "lead", "leaf", 
    "league", "lean", "leap", "learn", "lease", "leather", "leave", "lecture", "ledger", 
    "left", "leg", "legacy", "legal", "legend", "lemon", "lens", "level", "lever", 
    "lib", "lid", "life", "lift", "light", "like", "limit", "line", "link", "lion", 
    "lip", "liquid", "list", "lite", "live", "load", "loan", "lobby", "local", "lock", 
    "locus", "lodge", "log", "logic", "logo", "loop", "lord", "lore", "lot", "loud", 
    "lounge", "love", "low", "loyalty", "luck", "lumen", "lunar", "lunch", "lung", 
    "lure", "lush", "lux", "lyric", "m", "machine", "macro", "mad", "magic", "magnet", 
    "mail", "main", "major", "make", "maker", "male", "man", "manage", "map", "marble", 
    "march", "mark", "market", "mars", "mart", "mask", "mass", "master", "match", 
    "mate", "material", "math", "matrix", "matter", "max", "may", "maze", "meal", 
    "mean", "measure", "meat", "mech", "medal", "media", "medic", "meet", "mega", 
    "mello", "melody", "melon", "melt", "memo", "memory", "mentor", "menu", "merch", 
    "merge", "merit", "mesh", "mess", "metal", "meter", "method", "metro", "micro", 
    "mid", "might", "mile", "milk", "mill", "mind", "mine", "mini", "mint", "minute", 
    "mirror", "miss", "mission", "mist", "mix", "mobile", "mode", "model", "modern", 
    "modul", "mom", "moment", "money", "monitor", "monkey", "mono", "monster", "month", 
    "mood", "moon", "moor", "more", "morning", "morph", "motion", "motor", "mount", 
    "mouse", "mouth", "move", "movie", "much", "mud", "mug", "mule", "multi", "muscle", 
    "muse", "music", "must", "mute", "mutual", "my", "myth", "n", "nail", "name", 
    "nano", "nap", "nation", "native", "nature", "nav", "near", "neat", "nebula", 
    "neck", "need", "needle", "neo", "neon", "nerd", "nest", "net", "network", "neur", 
    "neutral", "new", "news", "next", "nexus", "nice", "niche", "night", "nimble", 
    "nine", "ninja", "nitro", "no", "noble", "node", "noise", "nomad", "noon", "north", 
    "nose", "note", "nova", "novel", "now", "nu", "nuke", "null", "number", "nurse", 
    "nut", "o", "oak", "oar", "oasis", "object", "ocean", "oct", "octa", "odd", "off", 
    "offer", "office", "oil", "ok", "old", "olive", "omega", "omni", "on", "one", 
    "onion", "only", "open", "opera", "optic", "option", "oracle", "orange", "orbit", 
    "order", "organ", "origin", "os", "out", "outlet", "output", "oval", "oven", 
    "over", "owl", "own", "owner", "oxide", "oxygen", "ozone", "p", "pace", "pack", 
    "packet", "pact", "pad", "page", "pair", "pal", "pale", "palm", "pan", "panda", 
    "panel", "panic", "paper", "para", "parade", "park", "part", "partner", "party", 
    "pass", "past", "patch", "path", "patrol", "pay", "peace", "peak", "pear", "pearl", 
    "pedal", "peer", "pen", "penguin", "people", "pepper", "per", "perfect", "perform", 
    "pet", "petal", "phase", "phone", "photo", "phrase", "phys", "pick", "picnic", 
    "picture", "pie", "piece", "pier", "pig", "pike", "pile", "pilot", "pin", "pine", 
    "pink", "pipe", "pit", "pitch", "pivot", "pixel", "place", "plain", "plan", "plane", 
    "planet", "plant", "plasma", "plate", "play", "plaza", "plea", "plex", "plot", 
    "plug", "plum", "plus", "pocket", "pod", "poem", "poet", "point", "polar", "pole", 
    "police", "policy", "poll", "polo", "poly", "pond", "pool", "pop", "port", "portal", 
    "pose", "posh", "post", "pot", "pound", "pour", "powder", "power", "practice", 
    "press", "price", "pride", "prime", "print", "prior", "prism", "prize", "pro", 
    "probe", "process", "prod", "profile", "profit", "prog", "project", "promo", "proof", 
    "prop", "proper", "proto", "proxy", "public", "pull", "pulse", "pump", "punch", 
    "punk", "pup", "pure", "purple", "push", "put", "puzzle", "pyramid", "pyro"
]

suffixes_raw = [
    "able", "ac", "ace", "acity", "act", "ad", "ade", "age", "ai", "aid", "al", "all", 
    "ally", "alpha", "an", "ance", "ant", "app", "arc", "arch", "art", "ary", "as", 
    "at", "ate", "atic", "ation", "ative", "ator", "base", "bay", "bee", "berry", 
    "best", "bet", "bit", "bite", "book", "bot", "box", "boy", "brain", "brand", 
    "buddy", "bug", "bus", "byte", "cab", "cafe", "camp", "can", "cap", "care", 
    "cart", "case", "cast", "cat", "center", "central", "chain", "chat", "check", 
    "choice", "city", "click", "cloud", "club", "co", "coach", "code", "coin", "com", 
    "con", "connect", "core", "corp", "craft", "crate", "crew", "cube", "cult", "cup", 
    "cut", "cycle", "dad", "daily", "dao", "dash", "data", "date", "day", "db", "deal", 
    "deck", "deep", "desk", "dev", "dig", "direct", "dish", "dna", "do", "doc", "dock", 
    "dog", "dom", "dome", "door", "dot", "draft", "drive", "drop", "dry", "duo", "dye", 
    "ease", "easy", "eat", "echo", "edge", "edit", "editor", "edu", "effect", "egg", 
    "ego", "electro", "element", "elite", "empire", "en", "end", "engine", "ent", 
    "enter", "entry", "env", "epic", "era", "ergo", "ery", "ess", "est", "et", "eth", 
    "eur", "eve", "event", "ever", "ex", "expert", "express", "eye", "fab", "face", 
    "fact", "factory", "fair", "fan", "farm", "fast", "feed", "fest", "field", "file", 
    "film", "fin", "finder", "fire", "firm", "first", "fish", "fit", "fix", "flag", 
    "flash", "flat", "fleet", "flex", "flight", "flip", "float", "flow", "flower", 
    "fluid", "flux", "fly", "focus", "fog", "fold", "folk", "folio", "food", "foot", 
    "force", "forge", "form", "fort", "forum", "found", "fox", "frame", "free", "fresh", 
    "friend", "front", "fruit", "fuel", "full", "fun", "fund", "fuse", "fusion", 
    "future", "fx", "g", "gain", "galaxy", "game", "gap", "garage", "garden", "gate", 
    "gear", "geek", "gem", "gen", "geo", "get", "ghost", "giant", "gig", "giga", 
    "glass", "glide", "global", "globe", "glow", "go", "goal", "gold", "golf", "good", 
    "goods", "goose", "gopher", "grade", "gram", "graph", "grass", "grid", "group", 
    "grow", "guard", "guide", "guild", "guru", "gym", "h", "habit", "hack", "hall", 
    "halo", "hand", "handle", "harbor", "hard", "hash", "hat", "haven", "hawk", 
    "head", "health", "heart", "heat", "heavy", "hedge", "hello", "help", "hero", 
    "hex", "hi", "high", "hike", "hill", "hint", "hip", "hire", "hit", "hive", 
    "hobby", "hold", "hole", "home", "honey", "hook", "hop", "hope", "horizon", 
    "horn", "host", "hotel", "hour", "house", "hub", "human", "hunt", "hut", "hydro", 
    "hyper", "i", "ia", "ian", "ible", "ic", "ice", "icon", "id", "idea", "ify", 
    "ignite", "image", "impact", "in", "inc", "index", "ine", "info", "ing", "ink", 
    "inn", "input", "insight", "instant", "intel", "inter", "io", "ion", "iq", "is", 
    "ism", "iso", "ist", "it", "ite", "ity", "ive", "ix", "ize", "jar", "java", 
    "jet", "job", "join", "joint", "joy", "js", "juice", "jump", "junction", "jungle", 
    "just", "karma", "keep", "key", "kick", "kid", "kin", "kind", "king", "kit", 
    "kite", "lab", "labs", "land", "lane", "lap", "last", "latch", "launch", "law", 
    "layer", "lead", "leaf", "lean", "leap", "learn", "ledger", "legal", "legend", 
    "lens", "level", "lever", "lib", "lid", "life", "lift", "light", "like", "limit", 
    "line", "link", "lion", "lip", "liquid", "list", "lite", "live", "load", "loan", 
    "local", "lock", "lodge", "log", "logic", "logo", "loop", "lord", "lore", "lot", 
    "loud", "lounge", "love", "low", "loyalty", "luck", "lumen", "lunar", "lunch", 
    "lung", "lure", "lux", "ly", "lyric", "m", "machine", "macro", "mad", "magic", 
    "magnet", "mail", "main", "maker", "man", "map", "mark", "market", "mart", 
    "mask", "mass", "master", "match", "mate", "matic", "matrix", "matter", "max", 
    "may", "maze", "meal", "mean", "measure", "meat", "mech", "medal", "media", 
    "medic", "meet", "mega", "melody", "melon", "melt", "memo", "memory", "mentor", 
    "menu", "merch", "merge", "merit", "mesh", "mess", "metal", "meter", "method", 
    "metro", "micro", "mid", "mile", "milk", "mill", "mind", "mine", "mini", "mint", 
    "minute", "mirror", "miss", "mission", "mist", "mix", "mobile", "mode", "model", 
    "modern", "modul", "mom", "moment", "money", "monitor", "monkey", "mono", "monster", 
    "month", "mood", "moon", "moor", "more", "morph", "motion", "motor", "mount", 
    "mouse", "mouth", "move", "movie", "much", "mud", "mug", "multi", "muse", "music", 
    "must", "mute", "my", "myth", "n", "nail", "name", "nano", "nap", "nation", 
    "native", "nature", "nav", "near", "neat", "nebula", "neck", "need", "needle", 
    "neo", "neon", "nerd", "nest", "net", "network", "neur", "neutral", "new", "news", 
    "next", "nexus", "nice", "niche", "night", "nimble", "nine", "ninja", "nitro", 
    "no", "noble", "node", "noise", "nomad", "noon", "north", "nose", "note", "nova", 
    "novel", "now", "nu", "nuke", "null", "number", "nurse", "nut", "o", "oak", 
    "oasis", "object", "ocean", "oct", "octa", "odd", "off", "offer", "office", "oil", 
    "ok", "old", "olive", "omega", "omni", "on", "one", "onion", "only", "open", 
    "opera", "optic", "option", "oracle", "orange", "orbit", "order", "organ", "origin", 
    "os", "out", "outlet", "output", "oval", "oven", "over", "owl", "own", "owner", 
    "oxide", "oxygen", "ozone"
]

# 2. HELPER FUNCTIONS TO ASSIGN METADATA

def get_vibe(word):
    # Simple heuristic to assign vibes based on characters/length
    if word.endswith('x') or word.endswith('z'): return "futuristic"
    if word.endswith('o') or word.endswith('a'): return "modern"
    if len(word) <= 3: return "minimalist"
    if "tech" in word or "soft" in word: return "technical"
    return "general"

def get_tags(word):
    tags = []
    if len(word) < 4: tags.append("short")
    if word[0] in 'aeiou': tags.append("vowel-start")
    # Add domain logic here
    if word in ["fin", "pay", "bank", "cash", "coin"]: tags.append("finance")
    if word in ["bio", "health", "med", "life"]: tags.append("health")
    if word in ["code", "soft", "dev", "stack", "git"]: tags.append("software")
    return tags if tags else ["general"]

# 3. BUILD THE DATASET

dataset = {
    "meta": {
        "project": "Open Source Startup Name Generator",
        "version": "1.0.0",
        "license": "MIT"
    },
    "data": {
        "prefixes": [],
        "roots": [],
        "suffixes": []
    }
}

for w in prefixes_raw:
    dataset["data"]["prefixes"].append({
        "token": w,
        "tags": get_tags(w),
        "vibe": get_vibe(w)
    })

for w in roots_raw:
    dataset["data"]["roots"].append({
        "token": w,
        "tags": get_tags(w),
        "category": "noun" # Simplified assumption
    })

for w in suffixes_raw:
    dataset["data"]["suffixes"].append({
        "token": w,
        "tags": get_tags(w),
        "vibe": get_vibe(w)
    })

# 4. SAVE TO FILE

total_tokens = len(prefixes_raw) + len(roots_raw) + len(suffixes_raw)
dataset["meta"]["total_count"] = total_tokens

with open('startup_names.json', 'w') as f:
    json.dump(dataset, f, indent=2)

print(f"Successfully generated 'startup_names.json' with {total_tokens} tokens.")
