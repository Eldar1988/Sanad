export default function textToLength (text) {
  text = text.trim()
  if( text.length <= 70) return text
  text = text.slice(0, 70)
  return text + "..."
}
