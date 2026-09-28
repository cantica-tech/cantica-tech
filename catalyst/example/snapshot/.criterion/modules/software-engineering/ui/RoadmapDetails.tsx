import type { ChainNode } from "catalyst-core";

export function RoadmapDetails({ node }: { node: ChainNode }) {
  if (node.kind !== "roadmap") return null;
  const clean = node.signedOffBy
    ? node.signedOffBy.replace(/^_+|_+$/g, "")
    : "";
  return (
    <section>
      <h2>Roadmap</h2>
      <p>
        {node.roadmapName}
        {node.roadmapRetired ? " (retired)" : ""}
      </p>
      {clean ? (
        <p>
          Signed off by: <em>{clean}</em>
        </p>
      ) : null}
      {node.notes ? <p>{node.notes}</p> : null}
    </section>
  );
}
