from pprint import pprint

def print_score_result(score_result):
    print("\n🔍 TruthScore:")
    print(f"Score: {score_result['score']}/100")
    if score_result['flags']:
        print("⚠️ Flags:", ", ".join(score_result['flags']))
    else:
        print("✅ No suspicious flags found.")

def print_link_results(link_results):
    print("\n🔗 Link Scanner Results:")
    if not link_results:
        print("✅ No links found in message.")
        return

    for result in link_results:
        print(f"- {result['url']}")
        if result['is_suspicious']:
            print("  ⚠️ Flags:", ", ".join(result['flags']))
        else:
            print("  ✅ Looks safe.")

def divider():
    print("\n" + "=" * 50 + "\n")
