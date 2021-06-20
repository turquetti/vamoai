// mosaico.tsx
import React from "react";
import "./Mosaico.scss";

export const Mosaico = ({ images }) => {
    return (
        <>
            {images.map((image) => {
                return (
                    <div className="mosaico">
                        <img src={image.image} alt="" />
                    </div>
                )
            })}
        </>
    )
}

// mosaico.scss
.mosaico img {
    width: 25%;
}


// exposition.scss
.content {
    column-count: 3;
    column-gap: 3rem;
}

// exposition.tsx
import React from "react";
import { graphql } from "gatsby";

import styles from "./exposition.module.scss";
import { MetaData } from "../../components/common/meta";
import { Layout } from "../../components/common";
import { Title } from "../../components/title/Title";
import { Mosaico } from "../../components/mosaico/Mosaico"

const Exposition = ({ data, location }) => {
    const expositionPage = data.allGhostPage.edges[0].node;
    const pageTitle = expositionPage.title;

    const expositionImages = expositionPage.html
    const htmlObject = document.createElement("div");
    htmlObject.innerHTML = expositionImages;
    const imgSrc = htmlObject.getElementsByTagName("img");
    const imgsUrl = [];

    for (let i = 0; i < imgSrc.length; i++) {
        imgsUrl.push({ image: imgSrc[i].src });
    }

    return (
        <>
            <MetaData data={data} location={location} type="profile" />
            <Layout>
                <div>
                    <Title title={pageTitle} />
                    <Mosaico images={imgsUrl} />
                    <div className={styles.content}>
                        {expositionPage.plaintext}
                    </div>
                    
                </div>
            </Layout>
        </>
    );
};

export default Exposition;

export const pageQuery = graphql`
    query GhostExpositionQuery($slug: String!) {
        allGhostPage(
            sort: { order: DESC, fields: [published_at] }
            filter: { slug: { eq: $slug } }
        ) {
            edges {
                node {
                    ...GhostPageFields
                }
            }
        }
    }
`;
