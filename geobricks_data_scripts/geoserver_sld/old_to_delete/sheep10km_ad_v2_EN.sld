<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>20120812</sld:Name>
            <sld:Title/>
                <FeatureTypeStyle>
                   <Rule>
                     <RasterSymbolizer>
                       <ColorMap type="intervals">
                         <ColorMapEntry color="#38A800" quantity="0.0000000000001" opacity="0.00000000000001" label="Heads"/>
                         <ColorMapEntry color="#8BD100" quantity="37.017" label="0 - 37.01" />
                         <ColorMapEntry color="#FFFF00" quantity="74.034" label="37.01 – 74.03" />
                         <ColorMapEntry color="#FF7F00" quantity="148.06" label="74.03 - 148.06" />
                         <ColorMapEntry color="#FF0000" quantity="9439.40" label="148.06 - 9,439.40" />
                       </ColorMap>
                     </RasterSymbolizer>
                   </Rule>
                </FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>